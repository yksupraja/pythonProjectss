from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your email server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'supraja2d@gmail.com'  # Replace with your email address
app.config['MAIL_PASSWORD'] = 'pndsmcfwifbnbhyv'  # Replace with your email password

mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    msg = Message('New Message from Contact Form',
                  sender='supraja2d@gmail.com',  # Replace with your email address
                  recipients=['supraja2d@gmail.com'])  # Replace with recipient email address

    msg.body = f"Name: {name}\nEmail: {email}\n\n{message}"

    mail.send(msg)

    return "Email sent successfully"

if __name__ == '__main__':
    app.run(port=8000, debug=True)


