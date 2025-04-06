import streamlit as st
import os

# Configuration de la page
st.set_page_config(page_title="Kelvin UTHAYAKUMAR", page_icon="💻", layout="centered")

# Liens pour les fichiers
PROFILE_IMG = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/profile.jpg"
LINKEDIN_URL = "https://www.linkedin.com/in/kelvinuthaya"
GITHUB_URL = "https://github.com/kelvinuthaya"
LINKEDIN_ICON = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/refs/heads/main/linkedin-logo-linkedin-icon-transparent-free-png.png"  # URL pour l'icône LinkedIn
GITHUB_ICON = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/refs/heads/main/25231.png"  # URL pour l'icône GitHub

# 🔹 Liens distincts pour le CV
CV_VIEWER_URL = "https://drive.google.com/file/d/1LxTADEJ9p328SygiEwQY33at4sL6ZR6g/preview"

CV_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=1LxTADEJ9p328SygiEwQY33at4sL6ZR6g"

# ✅ Ajout de styles CSS avec correction de l'écrasement des icônes
st.markdown("""
    <style>
        .profile-img {
            position: fixed;
            top: 50px;
            right: 50px;
            border-radius: 50%;
            border: 3px solid #4CAF50;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            width: 80px;
            height: 80px;
        }

        .social-icons {
            position: fixed;
            top: 150px;
            right: 50px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .social-icons a {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: white;
            border: 2px solid #007BFF;
            transition: background-color 0.3s, color 0.3s;
        }

        .social-icons a:hover {
            background-color: #007BFF;
        }

        .social-icons img {
            width: 30px;
            height: 30px;
            object-fit: contain; /* Empêche l'écrasement */
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

# Affichage de la photo de profil
st.markdown(f'<img src="{PROFILE_IMG}" class="profile-img" />', unsafe_allow_html=True)

# 🔹 Icônes LinkedIn et GitHub sous la photo de profil avec des images
st.markdown(f"""
    <div class="social-icons">
        <a href="{LINKEDIN_URL}" target="_blank" title="Mon LinkedIn">
            <img src="{LINKEDIN_ICON}" alt="LinkedIn"/>
        </a>
        <a href="{GITHUB_URL}" target="_blank" title="Mon GitHub">
            <img src="{GITHUB_ICON}" alt="GitHub"/>
        </a>
    </div>
""", unsafe_allow_html=True)

# 📄 **Mon CV**
st.title("📄 Mon CV")
st.write("Vous pouvez consulter mon CV ci-dessous ou le télécharger.")

# 🔹 Affichage du CV en iframe
st.markdown(f'<iframe src="{CV_VIEWER_URL}" width="700" height="800"></iframe>', unsafe_allow_html=True)

# 📥 **Bouton de téléchargement du CV**
if st.button('📥 Télécharger mon CV'):
    st.markdown(f"[Télécharger le CV ici]({CV_DOWNLOAD_URL})", unsafe_allow_html=True)

# 📂 **Projets**
st.title("📂 Mes Projets")
st.subheader("🌐 Projet MSI - Analyse et Visualisation de Données")
st.write("""
Mon projet **AAD - MSI** est une application interactive développée avec **Streamlit**. Elle permet de gérer et visualiser des données sur des brevets concernant la 6G via une interface simple et intuitive.
""")
st.markdown("[Voir le projet AADMSI ici](https://aadmsi.streamlit.app)", unsafe_allow_html=True)

# 📸 **Capture d'écran du projet**
st.image("https://github.com/kelvinuthaya/KELVINUTK/blob/main/Capture%20d%E2%80%99e%CC%81cran%202025-03-20%20a%CC%80%2011.32.41.png?raw=true", caption="Capture d'écran du projet AADMSI", use_container_width=True)

# 🛠️ **Compétences et Technologies**
st.title("🛠️ Compétences et Technologies")
st.write("""
- **Langages de programmation** : Python, Java, JavaScript, SQL
- **Frameworks et outils** : Django, Flask, Streamlit, React, Node.js
- **Bases de données** : MySQL, MongoDB
- **Outils de développement** : Git, Docker, CI/CD, VS Code
- **Analyse de données** : Pandas, NumPy, Matplotlib, Seaborn
- **Cloud** : AWS, Heroku
""")

# 📚 **Formation**
st.title("📚 Formation")
st.write("""
- **2023 - Présent** : Bachelor en Informatique (BUT) - Université [Nom de l'Université]
- **2020 - 2023** : Bac S, spécialité Mathématiques - Lycée [Nom du Lycée]
""")

# 💼 **Soft Skills**
st.title("💼 Soft Skills")
st.write("""
- **Travail en équipe** : Expérience dans des projets collaboratifs, bonne communication et écoute.
- **Résolution de problèmes** : Aptitude à trouver des solutions créatives pour surmonter des défis techniques.
- **Gestion du temps** : Capacité à gérer plusieurs projets en parallèle tout en respectant les délais.
- **Adaptabilité** : Flexibilité dans l'adoption de nouvelles technologies et méthodes de travail.
""")

# 📬 **Me Contacter**
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
