from flask import Flask, request
import requests

app = Flask(__name__)

API_URL = "https://API-SERVICE-URL.onrender.com/selam"

@app.route("/", methods=["GET", "POST"])
def index():
    sonuc = ""

    if request.method == "POST":
        try:
            isim = request.form.get("isim")
            sehir = request.form.get("sehir")

            r = requests.post(
                API_URL,
                json={"isim": isim, "sehir": sehir},
                timeout=5
            )

            if r.status_code == 200:
                sonuc = r.json().get("mesaj", "Mesaj alınamadı")
            else:
                sonuc = "API servis hata verdi"
