from bottle import route, run, request, template, static_file
import smtplib
@route("/page")


def html():

    return template(r"C:\Users\maroc\Desktop\ECOLE\Ambulance\AmbulanceDeNuit.html")


@route('/static/<filename:path>')


def css(filename):

    return static_file(filename, root= r'C:\Users\maroc\Desktop\ECOLE\Ambulance\static')


@route("/resultat", method="post")


def principale():

    Vehicules = request.forms.get("Transport")

    date = request.forms.get("Quand")

    appt = request.forms.get("appt")

    if Vehicules == "Ambulance":

        return envoie_mail_Ambulance(Vehicules,date, appt)

    else:

        return envoie_mail_vsl(Vehicules,date, appt)


def envoie_mail_Ambulance(Vehicules,date, appt):
    gmail_user = "ambulancdedenuitmail@gmail.com"
    gmail_pwd = "L'ambulance159"
    FROM = 'ambulancdedenuitmail@gmail.com'
    TO = ['Marocato92@gmail.com']
    SUBJECT = "Commande"
    TEXT = "Commande le "+ date + " à " + appt + " en " + Vehicules
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message.encode())
        server.close()
        print('successfully sent the mail')
    except :
        print("failed to send mail")
        print(message)

    return template(r'C:\Users\maroc\Desktop\ECOLE\Ambulance\annexe.html')


def envoie_mail_vsl(Vehicules,date, appt):
    gmail_user = "ambulancdedenuitmail@gmail.com"
    gmail_pwd = "L'ambulance159"
    FROM = 'ambulancdedenuitmail@gmail.com'
    TO = ['Marocato92@gmail.com']
    SUBJECT = "Commande"
    TEXT = "Commande le "+ date + " à " + appt + " en " + Vehicules
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message.encode())
        server.close()
        print('successfully sent the mail')
    except :
        print("failed to send mail")
        print(message)

    return template(r'C:\Users\maroc\Desktop\ECOLE\Ambulance\annexe2.html')


run(host="localhost", port=8080)