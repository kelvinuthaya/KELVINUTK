import streamlit as st
import requests
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="Mon Portfolio", page_icon="💻", layout="wide")

# Liens GitHub (remplace avec ton repo)
PROFILE_IMG = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/profile.jpg"
CV_PREVIEW = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/refs/heads/main/Capture%20d’écran%202025-03-19%20à%2023.27.07.png"
CV_URL = "https://drive.google.com/file/d/11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx/preview"  # Lien de prévisualisation du PDF sur Google Drive

# Affichage des images avec contrôle d'erreur
st.title("Bienvenue sur mon Portfolio ! 👋")

# Style pour le défilement fluide
st.markdown("""
    <style>
        html {
            scroll-behavior: smooth;
        }
    </style>
""", unsafe_allow_html=True)

# Création des ancres pour chaque section
st.markdown("<a name='section1'></a>", unsafe_allow_html=True)  # Ancre pour Accueil
# Section Accueil
st.title("Bienvenue sur mon Portfolio ! 👋")
st.write("""
Bonjour ! Je suis Kelvin UTHAYAKUMAR, étudiant(e) en BUT Informatique et actuellement à la recherche d'un **stage** d'une durée de 8 à 10 semaines.  
Passionné(e) par le développement et les nouvelles technologies, voici mon portfolio où vous trouverez mon **CV**, mes **projets**, et mes **coordonnées**.
""")

st.image(PROFILE_IMG, width=250)
st.subheader("🚀 Explorez mon portfolio en faisant défiler la page !")

# Lien de navigation vers "Mon CV"
st.markdown("""
    <a href="#section2" style="font-size:20px; color: blue;">Voir mon CV 📄</a><br>
    <a href="#section3" style="font-size:20px; color: blue;">Voir mes projets 💻</a><br>
    <a href="#section4" style="font-size:20px; color: blue;">Me contacter 📬</a>
""", unsafe_allow_html=True)

st.markdown("<a name='section2'></a>", unsafe_allow_html=True)  # Ancre pour Mon CV
# Page CV
st.title("📄 Mon CV")
st.write("Vous pouvez consulter mon CV ci-dessous ou le télécharger.")
try:
    # 🔹 Affichage direct du PDF avec un iframe
    pdf_viewer = f'<iframe src="{CV_URL}" width="700" height="800"></iframe>'
    st.markdown(pdf_viewer, unsafe_allow_html=True)
    
    # 🔹 Bouton de téléchargement avec lien direct
    st.download_button(
        label="📥 Télécharger mon CV",
        data=requests.get(CV_URL).content,  # Télécharge le contenu du fichier PDF
        file_name="mon_cv.pdf",
        mime="application/pdf",
        key="download_cv"
    )
except Exception as e:
    st.error(f"❌ Impossible de charger le CV. Erreur: {e}")

st.markdown("<a name='section3'></a>", unsafe_allow_html=True)  # Ancre pour Projets
# Page Projets
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

st.markdown("<a name='section4'></a>", unsafe_allow_html=True)  # Ancre pour Contact
# Page Contact
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
