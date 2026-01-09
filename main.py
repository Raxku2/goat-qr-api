from qrcode import QRCode, constants
from qrcode.image.svg import SvgPathImage
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, RedirectResponse, JSONResponse
from io import BytesIO
from gc import collect

app = FastAPI(title="GOΔT Qr Generator", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    """Home route redirect to /Docs"""
    return RedirectResponse("/docs")


@app.get("/health")
def health():
    """API Health Check"""
    return JSONResponse({"status": "up"})


@app.get("/qr")
def generateQR(url: str, version: int = 2, box_size: int = 10, border: int = 4):
    """Generate a black on white qr code"""

    collect()

    if 1 > version or version > 40:
        version = 2

    if not url:
        return JSONResponse(
            content={
                "data": None,
                "message": "Error",
                "error_type": "No Params Provided",
            },
            status_code=400,
        )

    try:
        qr = QRCode(
            version=version,
            error_correction=constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=border,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(
            image_factory=SvgPathImage,
            factory_kwargs={"background": "white", "fill": "#000000"},
        )
        buf = BytesIO()
        img.save(buf)

        del qr
        collect()

        buf.seek(0)

        return StreamingResponse(
            content=buf,
            status_code=200,
            media_type="image/svg+xml",
            # headers={"Content-Disposition": 'attachment; filename="qr_code.svg"'},
        )
    except Exception as err:
        return JSONResponse(
            content={"data": None, "message": "Error", "error_type": str(err)},
            status_code=500,
        )
