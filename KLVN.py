import streamlit as st
import pandas as pd
import os

# Configuration de la page
st.set_page_config(page_title="Kelvin UTHAYAKUMAR", page_icon="💻", layout="centered")

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
            text-align: justify
