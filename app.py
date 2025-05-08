# VXP & Verve Backend (Python + Flask + JS + HTML Frontend Integration)
# This plan includes routing, automation, page linking, and email handling.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')  # VXP homepage

# Sign In Page
@app.route('/signin')
def signin():
    return render_template('signinindex.html')

# Handle login form
@app.route('/login', methods=['POST'])
def login():
    # This is placeholder logic for login verification
    email = request.form['email']
    password = request.form['password']
    # Real validation logic should be added here
    return redirect(url_for('dashboard'))

# Dashboard Page after login
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # new animated homepage with links

# Services Page (Services coming soon indicated)
@app.route('/services')
def services():
    return render_template('services.html')

# Blog Page
@app.route('/blog')
def blog():
    return render_template('blog.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Handle contact form and send email
@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    sender_email = '@gmail.com'  # your email
    sender_password = 'your-email-password'  # your password
    receiver_email = 'vxpservices81@gmail.com'  # VXP email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"New VXP Message from {name}"

    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
