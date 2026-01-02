from flask import Flask, request
import requests

app = Flask(__name__)

API_URL = "https://API-SERVICE-URL.onrender.com/selam"

@app.route("/", methods=["GET", "POST"])
def index():
    sonuc = ""

    if request.method == "POST":
        try:
            isim = request.form["isim"]
            sehir = request.form["sehir"]

            r = requests.post(
                API_URL,
                json={"isim": isim, "sehir": sehir},
                timeout=5
            )

            if r.status_code == 200:
                sonuc = r.json().get("mesaj", "Mesaj alınamadı")
            else:
                sonuc = "API servis hata verdi"

        except Exception:
            sonuc = "API bağlantı hatası"

    return f"""
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>Mikro Hizmetli Selam</title>
</head>
<body style="font-family:Arial; background:#202020; color:white; text-align:center; padding-top:40px;">
<h2>🌐 Mikro Hizmetli Selam Servisi</h2>

<form method="POST">
<input type="text" name="isim" placeholder="Adınız" required><br><br>
<input type="text" name="sehir" placeholder="Şehriniz" required><br><
