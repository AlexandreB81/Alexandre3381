import ssl
import socket
import datetime
import smtplib
from email.mime.text import MIMEText

def get_ssl_expiry_date(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            return expiry_date

def send_alert_email(subject, message, to_email):
    from_email = "your_email@gmail.com"  # Remplacez par votre e-mail
    from_password = "your_password"  # Remplacez par votre mot de passe
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, [to_email], msg.as_string())
        server.quit()
        print("Alerte envoyée avec succès.")
    except Exception as e:
        print("Erreur lors de l'envoi de l'alerte:", e)

def check_certificate_expiry(hostname, days_threshold=30):
    try:
        expiry_date = get_ssl_expiry_date(hostname)
        remaining_days = (expiry_date - datetime.datetime.utcnow()).days
        print(f"Le certificat de {hostname} expire dans {remaining_days} jours ({expiry_date}).")
        
        if remaining_days <= days_threshold:
            subject = f"Alerte: Expiration imminente du certificat SSL ({hostname})"
            message = f"Le certificat SSL de {hostname} expire dans {remaining_days} jours ({expiry_date}). Pensez à le renouveler."
            send_alert_email(subject, message, "recipient@example.com")  # Remplacez par l'e-mail du destinataire
    except Exception as e:
        print("Erreur lors de la vérification du certificat:", e)

# Exemple d'utilisation
check_certificate_expiry("example.com", days_threshold=15)
