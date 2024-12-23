from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/destinations')
def destinations():
    return render_template('destinations.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/submit-contact', methods=['POST'])
def submit_contact():
   
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone')  
    message = request.form['message']

    
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Message: {message}")

    
    return redirect(url_for('success'))


@app.route('/success')
def success():
    return "Thank you for contacting us! We will get back to you soon."




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       
        username = request.form['username']
        password = request.form['password']

      
        if username == 'admin' and password == 'password':
            return redirect(url_for('home'))  
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)

    return render_template('login.html')





@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle form submission here
        return "Signup successful!"
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
