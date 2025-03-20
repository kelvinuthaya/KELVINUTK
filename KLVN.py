import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Formulaire de contact
st.title("📬 Me Contacter")
st.write("N'hésitez pas à me contacter !")

nom = st.text_input("Votre nom")
email = st.text_input("Votre adresse email")
message = st.text_area("Votre message")

if st.button("Envoyer"):
    if nom and email and message:
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = "ton.email@example.com"  # Votre adresse email
        msg['Subject'] = f"Message de {nom}"

        body = f"Nom: {nom}\nEmail: {email}\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login('votre.email@gmail.com', 'votre_mot_de_passe')
                text = msg.as_string()
                server.sendmail(email, "ton.email@example.com", text)
            st.success("Message envoyé avec succès !")
        except Exception as e:
            st.error(f"Erreur lors de l'envoi : {str(e)}")
    else:
        st.warning("Veuillez remplir tous les champs.")
