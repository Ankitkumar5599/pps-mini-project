from flask import Flask, redirect, render_template, request, url_for
import string
import random
import pyperclip

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', generated_password="")

@app.route('/generate', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    use_uppercase = 'uppercase' in request.form
    use_lowercase = 'lowercase' in request.form
    use_numbers = 'numbers' in request.form
    use_symbols = 'symbols' in request.form

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return render_template('index.html', generated_password="Please select at least one option.")

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return render_template('index.html', generated_password=generated_password)

@app.route('/copy_password', methods=['POST'])
def copy_password():
    password_to_copy = request.form['password_to_copy']
    pyperclip.copy(password_to_copy)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

