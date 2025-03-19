import streamlit as st
import requests
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="Mon Portfolio", page_icon="💻", layout="wide")

# Liens GitHub (remplace avec ton repo)
PROFILE_IMG = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/profile.jpg"
CV_PREVIEW = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/refs/heads/main/Capture%20d’écran%202025-03-19%20à%2023.27.07.png"
CV_URL = "https://drive.google.com/file/d/11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx/view?usp=share_link"

# Affichage des images avec contrôle d'erreur
st.title("Bienvenue sur mon Portfolio ! 👋")

# Style CSS intégré pour personnaliser l'apparence
st.markdown("""
    <style>
        /* Définir la police principale pour tout le corps du texte */
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f4f9;  /* Couleur d'arrière-plan */
            color: #333333;  /* Couleur du texte principal */
        }
        
        /* Style pour les titres principaux */
        h1, h2, h3 {
            font-family: 'Verdana', sans-serif;
            color: #4CAF50;  /* Couleur verte pour les titres */
        }
        
        /* Style des liens de navigation */
        a {
            color: #6200ea;  /* Couleur des liens */
            font-weight: bold;
            text-decoration: none;
        }

        a:hover {
            color: #3700b3;  /* Couleur au survol */
        }

        /* Personnalisation des boutons */
        .stButton>button {
            background-color: #6200ea;  /* Bouton violet */
            color: white;  /* Texte du bouton en blanc */
            border-radius: 12px;  /* Coins arrondis */
            padding: 12px 24px;
            font-size: 16px;
            border: none;
        }
        
        /* Effet sur le bouton au survol */
        .stButton>button:hover {
            background-color: #3700b3;  /* Couleur du bouton au survol */
        }

        /* Personnalisation des images */
        img {
            border-radius: 50%;  /* Image circulaire */
            border: 5px solid #4CAF50;  /* Bordure verte autour de l'image */
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);  /* Ombre sous l'image */
        }
        
        /* Style pour le texte des sections */
        .section-text {
            font-size: 18px;
            line-height: 1.8;
            margin-top: 20px;
        }
        
        /* Style de la barre latérale */
        .css-1d391kg {
            background-color: #6200ea;  /* Couleur de fond de la sidebar */
        }
        .css-1d391kg .css-ffhzg2 {
            color: white;  /* Texte de la sidebar en blanc */
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

# Affichage de la photo de profil
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

    # 🔹 Bouton de téléchargement
    response = requests.get(CV_URL)
    response.raise_for_status()
    pdf_bytes = BytesIO(response.content)

    st.download_button(
        label="📥 Télécharger mon CV",
        data=pdf_bytes,
        file_name="mon_cv.pdf",
        mime="application/pdf",
        key="download_cv"
    )

except Exception as e:
    st.error(f"❌ Impossible de charger le CV. Erreur : {e}")

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

