from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba, Buluttan Selam!"

# 🔴 ÇOK ÖNEMLİ
application = app
