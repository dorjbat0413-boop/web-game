# =========================
# MINI GAMES WEB APP (Flask)
# =========================
# Run in VS Code
# 1. pip install flask
# 2. python app.py
# 3. Open http://127.0.0.1:5000

from flask import Flask, render_template_string, request, redirect, url_for
import random

app = Flask(__name__)

# ------------------ MAIN PAGE ------------------
home_html = """
<!DOCTYPE html>
<html>
<head>
<title>Mini Games</title>
<style>
body { font-family: Arial; background: linear-gradient(135deg,#1e3c72,#2a5298); color:white; text-align:center; }
.container { margin-top:50px; }
button { padding:15px; margin:10px; border:none; border-radius:10px; font-size:16px; cursor:pointer; }
button:hover { transform:scale(1.1); }
</style>
</head>
<body>
<div class="container">
<h1>🎮 MINI GAMES</h1>
<form action="/guess"><button>1. Санасан тоог таах</button></form>
<form action="/rps"><button>2. Хайч Чулуу Даавуу</button></form>
<form action="/image"><button>3. Зураг таах</button></form>
<form action="/fibo"><button>4. Фибоначчи</button></form>
<form action="/maze"><button>5. Төөрдөг байшин</button></form>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(home_html)

# ------------------ GAME 1 ------------------
@app.route("/guess", methods=["GET","POST"])
def guess():
    result = ""
    if request.method == "POST":
        num = int(request.form["num"])
        secret = random.randint(1,10)
        if num == secret:
            result = "🎉 Зөв!"
        else:
            result = f"❌ Буруу! Зөв нь {secret}"
    return render_template_string("""
    <h2>Санасан тоо (1-10)</h2>
    <form method="post">
        <input name="num" type="number" required>
        <button>Таах</button>
    </form>
    <p>{{result}}</p>
    <a href="/">Back</a>
    """, result=result)

# ------------------ GAME 2 ------------------
@app.route("/rps", methods=["GET","POST"])
def rps():
    choices = ["хайч","чулуу","даавуу"]
    result = ""
    if request.method == "POST":
        user = request.form["choice"]
        comp = random.choice(choices)
        if user == comp:
            result = "Тэнцлээ"
        elif (user=="хайч" and comp=="даавуу") or (user=="чулуу" and comp=="хайч") or (user=="даавуу" and comp=="чулуу"):
            result = "🎉 Та хожлоо"
        else:
            result = "❌ Та хожигдлоо"
        result += f" (Компьютер: {comp})"
    return render_template_string("""
    <h2>Хайч Чулуу Даавуу</h2>
    <form method="post">
        <button name="choice" value="хайч">✂️</button>
        <button name="choice" value="чулуу">🪨</button>
        <button name="choice" value="даавуу">📄</button>
    </form>
    <p>{{result}}</p>
    <a href="/">Back</a>
    """, result=result)

# ------------------ GAME 3 ------------------
@app.route("/image", methods=["GET","POST"])
def image():
    answer = "cat"
    result = ""
    if request.method == "POST":
        guess = request.form["guess"]
        result = "🎉 Зөв" if guess.lower()==answer else "❌ Буруу"
    return render_template_string("""
    <h2>Зураг таах</h2>
    <img src="https://placekitten.com/200/200">
    <form method="post">
        <input name="guess" placeholder="Юу вэ?">
        <button>Таах</button>
    </form>
    <p>{{result}}</p>
    <a href="/">Back</a>
    """, result=result)

# ------------------ GAME 4 ------------------
@app.route("/fibo", methods=["GET","POST"])
def fibo():
    result=""
    if request.method=="POST":
        n=int(request.form["n"])
        a,b=0,1
        seq=[]
        for _ in range(n):
            seq.append(a)
            a,b=b,a+b
        result = seq
    return render_template_string("""
    <h2>Фибоначчи дараалал</h2>
    <form method="post">
        <input name="n" type="number" placeholder="n">
        <button>Бодох</button>
    </form>
    <p>{{result}}</p>
    <a href="/">Back</a>
    """, result=result)

# ------------------ GAME 5 ------------------
@app.route("/maze")
def maze():
    return render_template_string("""
    <h2>Төөрдөг байшин (Demo)</h2>
    <p>⬜⬜⬛⬜⬜</p>
    <p>⬛⬜⬛⬜⬛</p>
    <p>⬜⬜⬜⬜⬜</p>
    <p>⬜⬛⬛⬛⬜</p>
    <p>⬜⬜⬜⬛🏁</p>
    <a href="/">Back</a>
    """)

# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)
