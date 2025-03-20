import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Kelvin UTHAYAKUMAR", page_icon="💻", layout="centered")

# Liens pour les fichiers
PROFILE_IMG = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/profile.jpg"
LINKEDIN_URL = "https://www.linkedin.com/in/kelvinuthaya"
GITHUB_URL = "https://github.com/kelvinuthaya"
CV_VIEWER_URL = "https://drive.google.com/file/d/11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx/preview"
CV_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx"
PROJECT_AADMSI_URL = "https://aadmsi.streamlit.app"
PROJECT_AADMSI_IMG = "https://via.placeholder.com/800x400?text=Capture+du+projet+AADMSI"

# ✅ Ajout de styles CSS
st.markdown("""
    <style>
        body { font-family: 'Helvetica', sans-serif; background-color: #f4f4f9; color: #333; }
        h1, h2, h3 { color: #4CAF50; }
        a { color: #007BFF; font-weight: bold; text-decoration: none; }
        a:hover { color: #0056b3; }

        .profile-img {
            position: fixed;
            top: 50px;
            right: 50px;
            border-radius: 50%;
            border: 3px solid #4CAF50;
            width: 50px;
            height: 50px;
        }

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

# 🔹 Menu de navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- [🏠 Accueil](#accueil)
- [📄 Mon CV](#mon-cv)
- [📂 Projets](#mes-projets)
- [🛠 Compétences](#compétences)
- [📬 Me Contacter](#me-contacter)
""", unsafe_allow_html=True)

# 🏠 **Accueil**
st.title("🏠 Accueil")
st.write("""
Bonjour ! Je suis **Kelvin UTHAYAKUMAR**, étudiant en **B.U.T Informatique**, passionné par le développement et l'analyse de données. 
Actuellement en recherche d'un **stage de 8 à 10 semaines à partir de juin 2025**, je souhaite mettre mes compétences en **Python, JavaScript et développement informatique** au service d'une entreprise dynamique et innovante.
""")

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
st.markdown(f'<iframe src="{CV_VIEWER_URL}" width="700" height="800"></iframe>', unsafe_allow_html=True)
st.markdown(f'<a href="{CV_DOWNLOAD_URL}" class="download-btn">📥 Télécharger mon CV</a>', unsafe_allow_html=True)

# 📂 **Projets**
st.title("📂 Mes Projets")
st.subheader("🔍 SAÉ - Acquisition Automatique de Données")
st.write("""
- Construction d’une base de données automatisée à partir de brevets académiques.
- Création d’un tableau de bord interactif avec Streamlit/Dash.
- Gestion automatique de fichiers Excel.
""")
st.markdown(f"[🔗 Voir le projet]({PROJECT_AADMSI_URL})", unsafe_allow_html=True)
st.image(PROJECT_AADMSI_IMG, caption="Projet Acquisition de Données", use_column_width=True)

# 🛠 **Compétences**
st.title("🛠 Compétences")
st.write("Python, Java, SQL, PHP, JavaScript, C, HTML/CSS")

# 📬 **Me Contacter**
st.title("📬 Me Contacter")
st.subheader("📧 Email")
st.write("[kelvinutk@gmail.com](mailto:kelvinutk@gmail.com)")
st.subheader("💼 LinkedIn")
st.write(LINKEDIN_URL)
st.subheader("🐍 GitHub")
st.write(GITHUB_URL)
st.subheader("📍 Localisation")
st.write("Noisy-le-Sec")
st.subheader("📞 Téléphone")
st.write("0782119837")
