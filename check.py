from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def check():
    return render_template('check.html', rows=4, columns=4)


@app.route('/<int:num>')
def check2(num):
    return render_template('check.html', rows=4, columns=int(num/2))


@app.route('/<int:rows>/<int:columns>')
def check3(rows, columns):
    return render_template('check.html', rows=int(rows/2), columns=int(columns/2))


if __name__ == "__main__":
    app.run(debug=True, port=5003)
