# 🐐 GOAT QR API

**GOAT QR API** is a high-performance, lightweight QR Code generation API built with **FastAPI** that generates **SVG-based QR codes** instantly.  
Designed for speed, simplicity, and scalability — deployable anywhere, usable everywhere.

> **Tagline:**  
> _“The Greatest Of All Time QR Generator — Fast, Clean, SVG-native.”_

---

## 🚀 Live Deployment

**Base URL:**  


[https://goat-qr-api.vercel.app](https://goat-qr-api.vercel.app)



---

## 📌 Features

- ⚡ Ultra-fast QR generation
- 🖼️ SVG output (scalable & print-ready)
- 🔒 High error correction (ERROR_CORRECT_H)
- 🌐 CORS-enabled (open for frontend usage)
- 🧠 Memory-optimized (manual garbage collection)
- 📦 Zero database, stateless API
- 📘 Auto-generated Swagger Docs

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework
- **qrcode** – QR code generation
- **SVG Path Renderer** – Crisp vector output
- **Uvicorn** – ASGI server
- **Vercel** – Serverless deployment

---

## 📂 Project Structure

```

.
├── main.py
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/goat-qr-api.git
cd goat-qr-api
````

### 2️⃣ Install dependencies

```bash
pip install fastapi qrcode[pil] uvicorn
```

### 3️⃣ Run the server

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Interactive Swagger UI:

```
/docs
```

Example:

```
https://goat-qr-api.vercel.app/docs
```

---

## 🔍 API Endpoints

### 🏠 Root

**GET /**
Redirects to Swagger documentation.

---

### ❤️ Health Check

**GET /health**

**Response**

```json
{
  "status": "up"
}
```

---

### 🔳 Generate QR Code

**GET /qr**

#### Query Parameters

| Parameter  | Type   | Default  | Description          |
| ---------- | ------ | -------- | -------------------- |
| `url`      | string | required | Data to encode in QR |
| `version`  | int    | 2        | QR version (1–40)    |
| `box_size` | int    | 10       | Size of each QR box  |
| `border`   | int    | 4        | Border thickness     |

#### Example Request

```bash
curl "https://goat-qr-api.vercel.app/qr?url=https://example.com"
```

#### Response

* **Content-Type:** `image/svg+xml`
* **Body:** SVG QR code

---

## 🧠 Error Handling

### Missing URL

```json
{
  "data": null,
  "message": "Error",
  "error_type": "No Params Provided"
}
```

### Internal Error

```json
{
  "data": null,
  "message": "Error",
  "error_type": "<exception message>"
}
```

---

## 🔐 CORS Policy

* All origins allowed (`*`)
* Only `GET` methods enabled
* Safe for frontend integrations

---

## 📜 License

This project uses a **custom proprietary license** designed to:

* Allow free usage
* Enforce mandatory author credit
* Ensure revenue sharing
* Enable legal enforcement in India

📄 **See `LICENSE.txt` for full terms**

---

## 👤 Author

**Pinaka**
Creator of GOAT QR API
India 🇮🇳

---

## 🌟 Acknowledgements

* FastAPI Community
* Python QRCode Maintainers
* Open-source contributors

---

## 🚧 Roadmap

* [ ] PNG output support
* [ ] Color customization
* [ ] Logo-embedded QR codes
* [ ] Rate limiting
* [ ] API key system

---

> “Build fast. Share freely. Credit honestly.” 🐐

