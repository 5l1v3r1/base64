import sys
import random
try:
    from flask import Flask, url_for, request, render_template
except ImportError:
    print("First install flask module")
    print("[-] pip install flask")
    sys.exit(0)
import base64
from os import system, name
from time import sleep
app = Flask(__name__)
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = r"""
$$\                     $$\                                      $$$$$$\  $$\   $$\ $$\      $$\           $$\
\__|                    $$ |                                    $$  __$$\ $$ |  $$ |$$ | $\  $$ |          $$ |
$$\  $$$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\  $$ /  \__|$$ |  $$ |$$ |$$$\ $$ | $$$$$$\  $$$$$$$\
$$ |$$  _____|$$  __$$\ $$  __$$\  \____$$\ $$  _____|$$  __$$\ $$$$$$$\  $$$$$$$$ |$$ $$ $$\$$ |$$  __$$\ $$  __$$\
$$ |$$ /      $$ /  $$ |$$ |  $$ | $$$$$$$ |\$$$$$$\  $$$$$$$$ |$$  __$$\ \_____$$ |$$$$  _$$$$ |$$$$$$$$ |$$ |  $$ |
$$ |$$ |      $$ |  $$ |$$ |  $$ |$$  __$$ | \____$$\ $$   ____|$$ /  $$ |      $$ |$$$  / \$$$ |$$   ____|$$ |  $$ |
$$ |\$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$$ |$$$$$$$  |\$$$$$$$\  $$$$$$  |      $$ |$$  /   \$$ |\$$$$$$$\ $$$$$$$  |
\__| \_______| \____$$ |\_______/  \_______|\_______/  \_______| \______/       \__|\__/     \__| \_______|\_______/
              $$\   $$ |
              \$$$$$$  |                                      web base64 tools v1.0
               \______/                                          wrote bye iwHH
                                        iran-cyber.net
                                            github.com/iwhh/base64
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" %(random.choice(colors), line, clear))
        sleep(0.05)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/decode", methods = ["GET", "POST"])
def decoder():
    if request.method == "POST":
        StrDec = request.form['string'].encode("utf-8")
        try:
            decoder = base64.b64decode(StrDec)
            return render_template("decode.html", decode=decoder.decode("utf-8"))
        except base64.binascii.Error:
            return render_template("decode.html", error="you can decode base64 strings ;)")
    elif request.method == "GET":
        return render_template("decode.html")

@app.route("/encode", methods = ["GET", "POST"])
def encoder():
    if request.method == "POST":
        StrEnc = request.form['string'].encode("utf-8")
        encoder = base64.b64encode(StrEnc)
        return render_template("encode.html", encode=encoder.decode("utf-8"))

    elif request.method == "GET":
        return render_template("encode.html")


if __name__ == "__main__":
    app.run(host="localhost", port="123456", debug=True)
    if name == "nt":
        system("cls")
    else:
        system("clear")
    logo()
