import streamlit as st
import os

# Configuration de la page
st.set_page_config(page_title="Kelvin UTHAYAKUMAR", page_icon="💻", layout="centered")

# Liens pour les fichiers
PROFILE_IMG = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/profile.jpg"

# 🔹 Liens distincts pour le CV
CV_VIEWER_URL = "https://drive.google.com/file/d/11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx/preview"
CV_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx"

# ✅ Ajout de styles CSS
st.markdown("""
    <style>
        body { font-family: 'Helvetica', sans-serif; background-color: #f4f4f9; color: #333; margin: 0; padding: 0; }
        h1, h2, h3 { color: #4CAF50; }
        a { color: #007BFF; font-weight: bold; text-decoration: none; }
        a:hover { color: #0056b3; }

        /* Photo de profil : petite et dans le coin supérieur droit */
        .profile-img {
            position: fixed;
            top: 50px;
            right: 50px;
            border-radius: 50%;
            border: 3px solid #4CAF50;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            width: 50px;
            height: 50px;
        }

        /* Boutons Streamlit : personnalisation du bouton "Télécharger mon CV" */
        .stButton > button {
            background-color: #6200ea;
            color: white;
            border-radius: 12px;
            padding: 12px 24px;
            font-size: 16px;
            border: none;
        }
        
        .stButton > button:hover {
            background-color: #3700b3;
        }

        /* Section de texte : occuper toute la largeur disponible */
        .section-text {
            font-size: 18px;
            line-height: 1.8;
            margin-top: 20px;
            text-align: justify;
        }

        /* Container central */
        .container {
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
            padding: 0 20px;
        }

        /* Styles généraux pour le contenu textuel */
        .content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: flex-start;
            width: 100%;
        }

        .content > h1, .content > h2, .content > h3 {
            text-align: left;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# 🏠 **Accueil**
st.title("Bienvenue sur mon Portfolio ! 👋")
st.write("""
Bonjour ! Je suis **Kelvin UTHAYAKUMAR**, étudiant en **BUT Informatique** et en recherche d'un **stage (8 à 10 semaines)**.  
Découvrez ici mon **CV**, mes **projets** et mes **coordonnées**.
""")
st.markdown("<h3 class='section-text'>🚀 Explorez mon portfolio en faisant défiler la page !</h3>", unsafe_allow_html=True)

# Affichage de la photo de profil dans le coin supérieur droit
st.markdown(f'<img src="{PROFILE_IMG}" class="profile-img" />', unsafe_allow_html=True)

# 🔹 Navigation rapide
st.markdown("""
    <div class='container'>
        <a href="#section2">📄 Voir mon CV</a><br>
        <a href="#section3">💻 Voir mes projets</a><br>
        <a href="#section4">📬 Me contacter</a><br>
        <a href="#section5">🛠️ Compétences et Technologies</a><br>
        <a href="#section6">📚 Formation</a><br>
        <a href="#section7">💼 Soft Skills</a>
    </div>
""", unsafe_allow_html=True)

# 📄 **Mon CV**
st.markdown("<a name='section2'></a>", unsafe_allow_html=True)
st.title("📄 Mon CV")
st.write("Vous pouvez consulter mon CV ci-dessous ou le télécharger.")

# 🔹 Affichage du CV en iframe
st.markdown(f'<iframe src="{CV_VIEWER_URL}" width="700" height="800"></iframe>', unsafe_allow_html=True)

# 📥 **Bouton de téléchargement du CV** (correctement stylisé)
if st.button('📥 Télécharger mon CV'):
    st.markdown(f"[Télécharger le CV ici]({CV_DOWNLOAD_URL})", unsafe_allow_html=True)

# 📂 **Projets**
st.markdown("<a name='section3'></a>", unsafe_allow_html=True)
st.title("📂 Mes Projets")

# Description et lien vers le projet AADMSI
st.subheader("🌐 Projet AADMSI - Analyse et Visualisation de Données")
st.write("""
Mon projet **AADMSI** est une application interactive développée avec **Streamlit**. Elle permet de gérer et visualiser des données d'entreprise via une interface simple et intuitive. Vous pouvez télécharger des fichiers de données et les analyser graphiquement.
""")

# Affichage du projet AADMSI en iframe
st.markdown("""
    <iframe src="https://aadmsi.streamlit.app" width="100%" height="800" frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)

# 🛠️ **Compétences et Technologies**
st.markdown("<a name='section5'></a>", unsafe_allow_html=True)
st.title("🛠️ Compétences et Technologies")
st.write("""
Voici un aperçu des compétences techniques que j'ai développées au cours de ma formation et de mes projets :
- **Langages de programmation** : Python, Java, JavaScript, SQL
- **Frameworks et outils** : Django, Flask, Streamlit, React, Node.js
- **Bases de données** : MySQL, MongoDB
- **Outils de développement** : Git, Docker, CI/CD, VS Code
- **Analyse de données** : Pandas, NumPy, Matplotlib, Seaborn
- **Cloud** : AWS, Heroku
""")

# 📚 **Formation**
st.markdown("<a name='section6'></a>", unsafe_allow_html=True)
st.title("📚 Formation")
st.write("""
- **2023 - Présent** : Bachelor en Informatique (BUT) - Université [Nom de l'Université]
- **2020 - 2023** : Bac S, spécialité Mathématiques - Lycée [Nom du Lycée]
""")

# 💼 **Soft Skills**
st.markdown("<a name='section7'></a>", unsafe_allow_html=True)
st.title("💼 Soft Skills")
st.write("""
- **Travail en équipe** : Expérience dans des projets collaboratifs, bonne communication et écoute.
- **Résolution de problèmes** : Aptitude à trouver des solutions créatives pour surmonter des défis techniques.
- **Gestion du temps** : Capacité à gérer plusieurs projets en parallèle tout en respectant les délais.
- **Adaptabilité** : Flexibilité dans l'adoption de nouvelles technologies et méthodes de travail.
""")

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
