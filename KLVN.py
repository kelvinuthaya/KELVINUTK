import streamlit as st
import requests
import pandas as pd
import os
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="Mon Portfolio", page_icon="💻", layout="wide")

# Liens pour les fichiers
PROFILE_IMG = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/profile.jpg"

# 🔹 Liens distincts pour le CV
CV_VIEWER_URL = "https://drive.google.com/file/d/11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx/preview"
CV_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx"

# 🔹 Fichier CSV pour stocker les messages
FICHIER_MESSAGES = "messages.csv"

# ✅ Ajout de styles CSS
st.markdown("""
    <style>
        body { font-family: 'Arial', sans-serif; background-color: #f4f4f9; color: #333; }
        h1, h2, h3 { color: #4CAF50; }
        a { color: #007BFF; font-weight: bold; text-decoration: none; }
        a:hover { color: #0056b3; }
        .stButton>button { background-color: #6200ea; color: white; border-radius: 12px; padding: 12px 24px; font-size: 16px; border: none; }
        .stButton>button:hover { background-color: #3700b3; }
        img { border-radius: 50%; border: 5px solid #4CAF50; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); }
        .section-text { font-size: 18px; line-height: 1.8; margin-top: 20px; }
        .container { text-align: center; }
    </style>
""", unsafe_allow_html=True)

# 🏠 **Accueil**
st.title("Bienvenue sur mon Portfolio ! 👋")
st.write("""
Bonjour ! Je suis **Kelvin UTHAYAKUMAR**, étudiant en **BUT Informatique** et en recherche d'un **stage (8 à 10 semaines)**.  
Découvrez ici mon **CV**, mes **projets** et mes **coordonnées**.
""")
st.image(PROFILE_IMG, width=250)
st.markdown("<h3 class='section-text'>🚀 Explorez mon portfolio en faisant défiler la page !</h3>", unsafe_allow_html=True)

# 🔹 Navigation rapide
st.markdown("""
    <div class='container'>
        <a href="#section2">📄 Voir mon CV</a><br>
        <a href="#section3">💻 Voir mes projets</a><br>
        <a href="#section4">📬 Me contacter</a>
    </div>
""", unsafe_allow_html=True)

# 📄 **Mon CV**
st.markdown("<a name='section2'></a>", unsafe_allow_html=True)
st.title("📄 Mon CV")
st.write("Vous pouvez consulter mon CV ci-dessous ou le télécharger.")

# 🔹 Affichage du CV en iframe
st.markdown(f'<iframe src="{CV_VIEWER_URL}" width="700" height="800"></iframe>', unsafe_allow_html=True)

# 🔹 Bouton de téléchargement du CV
st.markdown(f"[📥 Télécharger mon CV]({CV_DOWNLOAD_URL})", unsafe_allow_html=True)

# 📂 **Projets**
st.markdown("<a name='section3'></a>", unsafe_allow_html=True)
st.title("📂 Mes Projets")

projets = [
    {"nom": "Site E-commerce", "desc": "Développement d'une boutique en ligne avec Django.", "lien": "https://github.com/tonprofil/projet1"},
    {"nom": "Application Mobile", "desc": "Application Android pour la gestion de tâches.", "lien": "https://github.com/tonprofil/projet2"},
    {"nom": "Chatbot IA", "desc": "Chatbot basé sur l'IA avec Python et GPT.", "lien": "https://github.com/tonprofil/projet3"},
]

for projet in projets:
    st.subheader(projet["nom"])
    st.write(projet["desc"])
    st.markdown(f"[🔗 Voir le projet]({projet['lien']})")

# 📬 **Me Contacter**
st.markdown("<a name='section4'></a>", unsafe_allow_html=True)
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

    st.subheader("🌍 Portfolio Web")
    st.write("[Mon Portfolio](https://tonportfolio.com)")

# 📩 **Formulaire de contact (enregistrement CSV)**
st.subheader("📨 Envoyer un message")

nom = st.text_input("Votre nom")
message = st.text_area("Votre message")

if st.button("Envoyer"):
    if nom and message:
        # Vérifier si le fichier existe, sinon créer une structure vide
        if os.path.exists(FICHIER_MESSAGES):
            df = pd.read_csv(FICHIER_MESSAGES)
        else:
            df = pd.DataFrame(columns=["Nom", "Message"])
        
        # Ajouter le message au fichier CSV
        nouveau_message = pd.DataFrame([[nom, message]], columns=["Nom", "Message"])
        df = pd.concat([df, nouveau_message], ignore_index=True)
        df.to_csv(FICHIER_MESSAGES, index=False)

        st.success("✅ Message envoyé et enregistré avec succès !")
    else:
        st.warning("⚠️ Veuillez remplir tous les champs.")

# 🔹 Voir les messages reçus (Admin uniquement)
if st.checkbox("📩 Voir les messages reçus (Admin)"):
    if os.path.exists(FICHIER_MESSAGES):
        df = pd.read_csv(FICHIER_MESSAGES)
        if not df.empty:
            st.write(df)
        else:
            st.info("Aucun message reçu pour le moment.")
    else:
        st.info("Aucun message reçu pour le moment.")