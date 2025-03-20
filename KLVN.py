import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Kelvin UTHAYAKUMAR", page_icon="💻", layout="centered")

# Liens pour les fichiers
PROFILE_IMG = "https://raw.githubusercontent.com/kelvinuthaya/KELVINUTK/4561e0f75ea1b2fce8894a1f6969dc30d5866fe7/profile.jpg"
LINKEDIN_URL = "https://www.linkedin.com/in/kelvinuthaya"
GITHUB_URL = "https://github.com/kelvinuthaya"
CV_VIEWER_URL = "https://drive.google.com/file/d/11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx/preview"
CV_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=11YKFjRfxwF55Ka_WOeKTyMZ_txJoG6bx"

# ✅ Ajout de styles CSS
st.markdown("""
    <style>
        body { font-family: 'Helvetica', sans-serif; background-color: #f4f4f9; color: #333; }
        h1, h2, h3 { color: #4CAF50; }
        a { color: #007BFF; font-weight: bold; text-decoration: none; }
        a:hover { color: #0056b3; }
    </style>
""", unsafe_allow_html=True)

# 🏠 **Accueil**
st.title("Bienvenue sur mon Portfolio ! 👋")
st.write("""
Bonjour ! Je suis **Kelvin UTHAYAKUMAR**, étudiant en **B.U.T Informatique** et en recherche d'un **stage (8 à 10 semaines) à partir de juin 2025**.
Découvrez ici mon **CV**, mes **projets** et mes **coordonnées**.
""")

# 📄 **Mon CV**
st.title("📄 Mon CV")
st.markdown(f'<iframe src="{CV_VIEWER_URL}" width="700" height="800"></iframe>', unsafe_allow_html=True)
st.markdown(f'<a href="{CV_DOWNLOAD_URL}" class="download-btn">📥 Télécharger mon CV</a>', unsafe_allow_html=True)

# 📂 **Projets Académiques**
st.title("📂 Mes Projets")
st.subheader("📊 SAÉ - Enquête et Analyse des Diplômés de l'IUT")
st.write("""
- Réalisation d’un questionnaire sur les poursuites d’études et les insertions professionnelles.
- Analyse et visualisation des données avec Python (Pandas, Matplotlib).
- Rédaction d’un rapport et présentation des résultats.
""")

st.subheader("🌍 Nuit de l’Info - Concours National")
st.write("""
- Développement d’une application web éducative interactive en une nuit.
- Collaboration en équipe pour créer une plateforme reliant systèmes humains et océaniques.
""")

st.subheader("🔍 SAÉ - Acquisition Automatique de Données")
st.write("""
- Construction d’une base de données automatisée à partir de brevets académiques.
- Création d’un tableau de bord interactif avec Streamlit/Dash.
- Gestion automatique de fichiers Excel.
""")

# 🛠 **Compétences**
st.title("🛠 Compétences")
st.subheader("💻 Informatique")
st.write("Python, Java, SQL, PHP, JavaScript, C, HTML/CSS")

st.subheader("📊 Outils Bureautiques")
st.write("Excel, Suite Office (Word, PowerPoint)")

st.subheader("🎨 Multimédia")
st.write("Final Cut Pro, Adobe Lightroom")

st.subheader("🗣 Langues")
st.write("Tamoul (bilingue), Anglais (B2), Espagnol (B2)")

# 📬 **Me Contacter**
st.title("📬 Me Contacter")
col1, col2 = st.columns(2)
with col1:
    st.subheader("📧 Email")
    st.write("[kelvinutk@gmail.com](mailto:kelvinutk@gmail.com)")
    
    st.subheader("💼 LinkedIn")
    st.write(f"[Mon LinkedIn]({LINKEDIN_URL})")
with col2:
    st.subheader("🐍 GitHub")
    st.write(f"[Mon GitHub]({GITHUB_URL})")
    
    st.subheader("📍 Localisation")
    st.write("Noisy-le-Sec")

st.subheader("📞 Téléphone")
st.write("0782119837")

