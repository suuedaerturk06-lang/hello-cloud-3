from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        isim = request.form["isim"]
        sehir = request.form["sehir"]

        return f"""
        <!DOCTYPE html>
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
