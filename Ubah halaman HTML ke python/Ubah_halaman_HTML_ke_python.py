from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('nm')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
