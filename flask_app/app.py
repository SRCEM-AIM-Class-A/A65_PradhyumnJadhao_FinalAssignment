from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hello, World!</h1>
        <p><a href="/form">Go to User Form</a></p>
    '''

@app.route('/form', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form.get('name', '')
        age = request.form.get('age', '')
        
        # Basic error handling
        if not name or not name.strip():
            return '<p style="color: red;">Error: Name cannot be empty.</p>' + render_template('form.html')
        
        try:
            age = int(age)
            if age <= 0 or age > 120:
                return '<p style="color: red;">Error: Age must be between 1 and 120.</p>' + render_template('form.html')
        except ValueError:
            return '<p style="color: red;">Error: Age must be a valid number.</p>' + render_template('form.html')
            
        return f'<h2>Hello, {name}! You are {age} years old.</h2>'
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')