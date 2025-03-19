import streamlit as st
import requests
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="Mon Portfolio", page_icon="💻", layout="wide")

# Liens GitHub (remplace avec ton repo)
PROFILE_IMG = "https://github.com/kelvinuthaya/KELVINUTK/blob/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/profile.jpg"
CV_PREVIEW = "https://raw.githubusercontent.com/tonprofil/tonrepo/main/images/cv_preview.png"
CV_URL = "https://github.com/kelvinuthaya/KELVINUTK/blob/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/CV.pdf"

# Affichage des images avec contrôle d'erreur
st.title("Bienvenue sur mon Portfolio ! 👋")

try:
    st.image(PROFILE_IMG, width=250, caption="Photo de profil")
except:
    st.error("Impossible de charger l'image de profil.")

try:
    response = requests.get(CV_URL)
    response.raise_for_status()
    pdf_bytes = BytesIO(response.content)
    st.download_button(label="📥 Télécharger mon CV", data=pdf_bytes, file_name="mon_cv.pdf", mime="application/pdf")
    st.image(CV_PREVIEW, caption="Aperçu du CV")
except:
    st.error("Impossible de charger le CV.")


# Sidebar pour la navigation
st.sidebar.title("Navigation")
pages = ["Accueil", "Mon CV", "Projets", "Contact"]
page = st.sidebar.radio("Aller à :", pages)

# Accueil
if page == "Accueil":
    st.title("Bienvenue sur mon Portfolio ! 👋")
    st.write("""
    Bonjour ! Je suis [Ton Nom], étudiant(e) en informatique et actuellement à la recherche d'un **stage** ou d'une **alternance**.  
    Passionné(e) par le développement et les nouvelles technologies, voici mon portfolio où vous trouverez mon **CV**, mes **projets**, et mes **coordonnées**.
    """)
    
    st.image(PROFILE_IMG, width=250)
    st.subheader("🚀 Explorez mon portfolio via le menu à gauche !")

# Page CV
elif page == "Mon CV":
    st.title("📄 Mon CV")
    st.write("Vous pouvez consulter mon CV ci-dessous ou le télécharger.")

    try:
        # Téléchargement du fichier PDF depuis GitHub
        response = requests.get(CV_URL)
        response.raise_for_status()
        pdf_bytes = BytesIO(response.content)

        # Bouton de téléchargement avec une clé unique pour éviter les conflits
        st.download_button(
            label="📥 Télécharger mon CV",
            data=pdf_bytes,
            file_name="mon_cv.pdf",
            mime="application/pdf",
            key="download_cv"  # Clé unique pour éviter l'erreur
        )

        # Affichage d'un aperçu du CV (image)
        st.image(CV_PREVIEW, caption="Aperçu du CV")

    except requests.exceptions.RequestException:
        st.error("Impossible de charger le CV. Vérifiez le lien GitHub.")

# Page Projets
elif page == "Projets":
    st.title("📂 Mes Projets")

    # Exemple de projets (remplace par les tiens)
    projets = [
        {"nom": "Site E-commerce", "desc": "Développement d'une boutique en ligne avec Django.", "lien": "https://github.com/tonprofil/projet1"},
        {"nom": "Application Mobile", "desc": "Application Android pour la gestion de tâches.", "lien": "https://github.com/tonprofil/projet2"},
        {"nom": "Chatbot IA", "desc": "Chatbot basé sur l'IA avec Python et GPT.", "lien": "https://github.com/tonprofil/projet3"},
    ]

    for projet in projets:
        st.subheader(projet["nom"])
        st.write(projet["desc"])
        st.markdown(f"[🔗 Voir le projet]({projet['lien']})")

# Page Contact
elif page == "Contact":
    st.title("📬 Me Contacter")

    st.write("N'hésitez pas à me contacter pour toute opportunité de stage ou alternance.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📧 Email")
        st.write("[ton.email@example.com](mailto:ton.email@example.com)")

        st.subheader("💼 LinkedIn")
        st.write("[Mon Profil LinkedIn](https://www.linkedin.com/in/tonprofil)")

    with col2:
        st.subheader("🐍 GitHub")
        st.write("[Mon GitHub](https://github.com/tonprofil)")

        st.subheader("🌍 Portefeuille Web")
        st.write("[Mon Portfolio](https://tonportfolio.com)")

    st.text_input("Votre nom")
    st.text_area("Votre message")
    if st.button("Envoyer"):
        st.success("Message envoyé avec succès ! (Simulé)")

# Lancer l'application avec : streamlit run app.py
