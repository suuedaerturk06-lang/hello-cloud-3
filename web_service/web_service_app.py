from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        isim = request.form["isim"]
        sehir = request.form["sehir"]

        return f'''<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Sonuç</title>
    <style>
        body {{
            font-family: Arial;
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .box {{
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}
        a {{
            text-decoration: none;
            color: #007bff;
        }}
    </style>
</head>
<body>
    <div class="box">
        <h2>Sonuç</h2>
        <p>Merhaba <b>{isim}</b>, <b>{sehir}</b> şehrinden!</p>
        <a href="/">↩ Geri dön</a>
    </div>
</body>
</html>'''

    return '''<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Form</title>
    <style>
        body {
            font-family: Arial;
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .box {
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            width: 300px;
        }
        input, button {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
        }
        button {
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>Bilgi Formu</h2>
        <form method="POST">
            <input name="isim" placeholder="Adınız" required>
            <input name="sehir" placeholder="Şehriniz" required>
            <button>Gönder</button>
        </form>
    </div>
</body>
</html>'''

if __name__ == "__main__":
    app.run(debug=True)
