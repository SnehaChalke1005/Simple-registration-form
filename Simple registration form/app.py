from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for registered users
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        users.append({'name': name, 'email': email})
        return redirect(url_for('users_list'))
    return render_template('register.html')

@app.route('/users')
def users_list():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
