from flask import Flask, render_template, request, redirect, url_for
import smtplib
import ssl


def send_mail(name, email, message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "madiprojvorona@gmail.com"  # Enter your address
    receiver_email = "madiprojvorona@gmail.com"  # Enter receiver address
    # password = input("Type your password and press enter: ")
    password = "n8zF67wkc7"
    message = """\
    Subject: mail

    {0}
    
    my email: {2}, {1}""".format(message, name, email)
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            return(1)
    except:
        return(0)

def send_comment(name, email, message, page):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "madiprojvorona@gmail.com"  # Enter your address
    receiver_email = "madiprojvorona@gmail.com"  # Enter receiver address
    # password = input("Type your password and press enter: ")
    password = "n8zF67wkc7"
    message = """\
    Subject: comment on {3}

    {0}
    
    my email: {2}, {1}""".format(message, name, email, page)
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            return(1)
    except:
        return(0)

app = Flask(__name__)


@app.route('/send-mail', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        name = request.form.get('name')  # access the data inside
        email = request.form.get('email')
        message = request.form.get('message')
        if send_mail(name, email, message):
            print("success")
        else:
            print("failed")
    return redirect(url_for('contact'))

@app.route('/comment', methods=['GET', 'POST'])
def commnet():
    if request.method == 'POST':
        name = request.form.get('name')  # access the data inside
        email = request.form.get('email')
        message = request.form.get('message')
        page = request.form.get('page')
        if send_comment(name, email, message, page):
            print("success")
        else:
            print("failed")
    return redirect(url_for(page))

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/project-detail")
def project_detail():
    return render_template("project-detail.html")


@app.route("/project-detail-2")
def project_detail_2():
    return render_template("project-detail-2.html")


@app.route("/project-detail-3")
def project_detail_3():
    return render_template("project-detail-3.html")


@app.route("/blog-detail")
def blog_detail():
    return render_template("blog-detail.html")


@app.route("/blog-detail-gaming")
def blog_detail_gaming():
    return render_template("blog-detail-gaming.html")


@app.route("/blog-detail-anime")
def blog_detail_anime():
    return render_template("blog-detail-anime.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000')
