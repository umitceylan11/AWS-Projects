from flask import Flask, render_template, request

def converter(sayi):
    Roma = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sayim=0
    for i in range(len(sayi)):
        if i+1 < len(sayi):
            if Roma[sayi[i]] < Roma[sayi[i+1]] :
                sayim=sayim-Roma[sayi[i]]
            else:
                sayim=sayim+Roma[sayi[i]]
        else:
            sayim=sayim+Roma[sayi[i]]
    return sayim
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hesap', methods = ["GET","POST"])
def hesap():
    if request.method == "POST":
        sayi = request.form.get("romarakami")
        cevap=converter(sayi)
        return render_template("number.html", cevap = cevap)
    else:
        return render_template("number.html")

if __name__=="__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)