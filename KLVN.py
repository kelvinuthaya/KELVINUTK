import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Kelvin UTHAYAKUMAR", page_icon="💻", layout="centered")

# Liens pour les fichiers
PROFILE_IMG = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/profile.jpg"
LINKEDIN_URL = "https://www.linkedin.com/in/tonprofil"
GITHUB_URL = "https://github.com/tonprofil"
CV_VIEWER_URL = "https://drive.google.com/file/d/11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx/preview"
CV_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx"

# ✅ Ajout de styles CSS
st.markdown("""
    <style>
        body { font-family: 'Helvetica', sans-serif; background-color: #f4f4f9; color: #333; }
        h1, h2, h3 { color: #4CAF50; }
        a { color: #007BFF; font-weight: bold; text-decoration: none; }
        a:hover { color: #0056b3; }

        /* Photo de profil */
        .profile-img {
            position: fixed;
            top: 50px;
            right: 50px;
            border-radius: 50%;
            border: 3px solid #4CAF50;
            width: 50px;
            height: 50px;
        }

        /* Icônes LinkedIn et GitHub */
        .social-icons {
            position: fixed;
            top: 110px;
            right: 50px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .social-icons a img {
            width: 30px;
            height: 30px;
        }

        /* Bouton Télécharger CV */
        .download-btn {
            display: inline-block;
            padding: 12px 20px;
            font-size: 16px;
            background-color: #6200ea;
            color: white;
            border-radius: 8px;
            text-align: center;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.3s;
        }
        .download-btn:hover {
            background-color: #3700b3;
        }

    </style>
""", unsafe_allow_html=True)

# 🏠 **Accueil**
st.title("Bienvenue sur mon Portfolio ! 👋")
st.write("""
Bonjour ! Je suis **Kelvin UTHAYAKUMAR**, étudiant en **BUT Informatique** et en recherche d'un **stage (8 à 10 semaines)**.  
Découvrez ici mon **CV**, mes **projets** et mes **coordonnées**.
""")

# 🔹 Photo de profil et icônes
st.markdown(f'<img src="{PROFILE_IMG}" class="profile-img" />', unsafe_allow_html=True)

st.markdown(f"""
    <div class="social-icons">
        <a href="{LINKEDIN_URL}" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo_2023.png" alt="LinkedIn">
        </a>
        <a href="{GITHUB_URL}" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/GitHub_Logo_2023.png" alt="GitHub">
        </a>
    </div>
""", unsafe_allow_html=True)

# 📄 **Mon CV**
st.title("📄 Mon CV")
st.write("Vous pouvez consulter mon CV ci-dessous ou le télécharger.")

# 🔹 Affichage du CV
st.markdown(f'<iframe src="{CV_VIEWER_URL}" width="700" height="800"></iframe>', unsafe_allow_html=True)

# 📥 **Bouton de téléchargement**
st.markdown(f'<a href="{CV_DOWNLOAD_URL}" class="download-btn">📥 Télécharger mon CV</a>', unsafe_allow_html=True)

# 📂 **Projets**
st.title("📂 Mes Projets")
st.subheader("🌐 Projet AADMSI - Analyse et Visualisation de Données")
st.write("""
Mon projet **AADMSI** est une application interactive développée avec **Streamlit**.  
Elle permet de gérer et visualiser des données d'entreprise.
""")
st.markdown("[🔗 Voir le projet AADMSI](https://aadmsi.streamlit.app)", unsafe_allow_html=True)

# 📸 Capture d'écran du projet
st.image("https://via.placeholder.com/800x400?text=Capture+du+projet+AADMSI", caption="Projet AADMSI", use_column_width=True)

# 📬 **Me Contacter**
st.title("📬 Me Contacter")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📧 Email")
    st.write("[ton.email@example.com](mailto:ton.email@example.com)")

    st.subheader("💼 LinkedIn")
    st.write(f"[Mon LinkedIn]({LINKEDIN_URL})")

with col2:
    st.subheader("🐍 GitHub")
    st.write(f"[Mon GitHub]({GITHUB_URL})")

    st.subheader("🌍 Portfolio Web")
    st.write("[Mon Portfolio](https://tonportfolio.com)")