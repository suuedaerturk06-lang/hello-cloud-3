from flask import Flask, request
import requests

app = Flask(__name__)

API_URL = "https://API-SERVICE-URL.onrender.com/selam"

@app.route("/", methods=["GET", "POST"])
def index():
    sonuc = ""

    if request.method == "POST":
        isim = request.form.get("isim")
        sehir = request.form.get("sehir")

        r = requests.post(API_URL, json={
            "isim": isim,
            "sehir": sehir
        })

        sonuc = r.json().get("mesaj")

    return f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Mikro Hizmetli Selam</title>
    <style>
        body {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            font-family: Arial;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }}
        .box {{
            background: rgba(0,0,0,0.3);
            padding: 30px;
            border-radius: 15px;
            width: 350px;
            text-align: center;
        }}
        input, button {{
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            border-radius: 8px;
            border: none;
        }}
        button {{
            background: #00ffd5;
            font-weight: bold;
        }}
        .sonuc {{
            margin-top: 15px;
            font-size: 18px;
        }}
    </style>
</head>
<body>
    <div class="box">
        <h2>🌐 Mikro Hizmetli Selam</h2>
        <form method="POST">
            <input type="text" name="isim" placeholder="Adınız" required>
            <input type="text" name="sehir" placeholder="Şehriniz" required>
            <button type="submit">Gönder</button>
        </form>
        <div class="sonuc">{sonuc}</div>
    </div>
</body>
</html>
"""
