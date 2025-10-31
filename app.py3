from flask import Flask, render_template_string, request
import os
import pyscog2

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", " ")

HTML = """
<!doctype html>
<html>
<head>
    <title>Buluttan Selam!</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
        h1 { color: #333; }
        form { margin: 20px auto; }
        input { padding: 10px; font size: 16px; }
        button { padding: 10px 15px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: painter; }
        ul { list-style: none; padding: 0; }
        li { background: white; margin: 5px auto; width: 200px; padding: 8px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Buluttan Selam!</h1>
    <p>Sueda,Selam! </p>
    <form method="POST">
        <input type= "text"  name= "isim" placeholder "Suedaa" required>
        <button type="submit">Gönder</button>
    </form>
    <h3>Ziayretçiler:</h3>
    <ul>
        {% for ad in isimler %}
            <li>{{ ad }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

def coonect_db ():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route("/", methods=["GET", "POST"])
def index ():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler ( id SERIAL PRIMARY KEY. isim TEXT)")

    if request.method == "POST":
       isim = request.form.get("isim")
       if isim :
           cur.execute("INSERT INTO ziyaretciler (isim) VALUES (%s)",(isim,))
           conn.commit()

cur.execute("INSERT INTO ziyaretciler ORDER BY id DESC LIMIT 10")
isimler = [row[0] for row in cur.fetchall()]

cur.close()
conn.close()
return render_template_string(HTML, isimler=isimler)

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000)
