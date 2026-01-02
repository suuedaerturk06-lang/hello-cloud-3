from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Form gönderildiyse
    if request.method == "POST":
        isim = request.form["isim"]
        sehir = request.form["sehir"]

        return f"""
        <h2>Sonuç</h2>
        <p>Merhaba {isim}, {sehir} şehrinden!</p>
        <a href="/">Geri dön</a>
        """

    # Sayfa ilk açıldığında
    return """
    <h2>Form</h2>
    <form method="POST">
        <input type="text" name="isim" placeholder="Adınızı yaz" required><br><br>
        <input type="text" name="sehir" placeholder="Şehrinizi yaz" required><br><br>
        <button type="submit">Gönder</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
