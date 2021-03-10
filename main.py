from flask import Flask, render_template, url_for, request, redirect
import smtplib

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

OWN_EMAIL = "你的 gmail 信箱"
OWN_PASSWORD = "你的密碼"

url_1_1 = "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2689&q=80" 
url_1_2 = "https://images.unsplash.com/photo-1517503733723-8ea1cf616798?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80"

@app.route('/', methods=["GET", "POST"])
def get_all_posts():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["subject"], data["message"])
        return render_template("index.html")
    
    return render_template("index.html")

@app.route('/portfolio')
def get_all_portfolio():
    return render_template("portfolio-details.html", url_1=url_1_1, url_2=url_1_2)

def send_email(name, email, subject, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nsubject: {subject}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)