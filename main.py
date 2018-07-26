from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def link_json_to_app():
    return render_template("charts.html")

if __name__ == "__main__":
    app.run(debug=True)





