from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('map.html')




if __name__ == "__main__":
    app.run()