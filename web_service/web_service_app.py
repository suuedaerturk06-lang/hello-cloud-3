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
            sehir = request.form
