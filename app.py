from flask import Flask, render_template, request

app = Flask(__name__)

def is_palindrome(s):
    return s == s[::-1]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        string = request.form['string']
        if is_palindrome(string):
            result = "The given string is a palindrome"
        else:
            result = "The given string is not a palindrome"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
