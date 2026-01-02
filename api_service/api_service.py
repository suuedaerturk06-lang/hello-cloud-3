from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/selam", methods=["POST"])
def selam():
    data = request.json
    isim = data["isim"]
    sehir = data["sehir"]

    return jsonify({
        "mesaj": f"Selam {isim}! {sehir} şehrinden bağlandığını gördüm 👋"
    })

if __name__ == "__main__":
    app.run()
