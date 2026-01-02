from flask import Flask, request  # <-- Bu satır mutlaka en üstte olmalı!
import requests

app = Flask(__name__)


# --- BU ÜÇ SATIRI EKLE ---
@app.route("/test")
def test():
    return "Uygulama Calisiyor!", 200
# -------------------------

# ÖNEMLİ: Kendi API servis URL'nizi buraya doğru yazdığınızdan emin olun
API_URL = "https://API-SERVICE-URL.onrender.com/selam"

@app.route("/", methods=["GET", "POST"])
def index():
    # ... (kodun geri kalanı aynı kalacak)

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
                sonuc = f"API servis hata verdi (Kod: {r.status_code})"

        except Exception as e:
            sonuc = f"API bağlantı hatası: {str(e)}"

    return f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mikro Hizmetli Selam</title>
</head>
<body style="font-family:Arial; background:#202020; color:white; text-align:center; padding-top:40px;">
    <h2>🌐 Mikro Hizmetli Selam Servisi</h2>

    <form method="POST" style="background: #333; display: inline-block; padding: 20px; border-radius: 10px;">
        <input type="text" name="isim" placeholder="Adınız" required style="padding: 8px; margin-bottom: 10px;"><br>
        <input type="text" name="sehir" placeholder="Şehriniz" required style="padding: 8px; margin-bottom: 10px;"><br>
        <button type="submit" style="padding: 10px 20px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer;">
            Gönder
        </button>
    </form>

    <div style="margin-top: 30px; font-size: 1.2em; color: #00ff00;">
        <strong>Sonuç:</strong> {sonuc}
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    # Render genellikle PORT çevresel değişkenini kullanır
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
