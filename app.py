
import streamlit as st
from docx import Document
from io import BytesIO

st.set_page_config(page_title="Générateur de CV SCC", layout="centered")

st.title("🧾 Générateur de CV format SCC")
st.write("Téléversez un fichier contenant les données du CV (Word .docx), et téléchargez une version formatée SCC.")

uploaded_file = st.file_uploader("📤 Téléverser un fichier Word contenant les données extraites", type=["docx"])

def extract_data(doc):
    data = {"certifications": [], "formations": [], "langues": [], "competences": [], "experiences": []}
    current = ""
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        if text.startswith("Certifications"):
            current = "certifications"
        elif text.startswith("Formations"):
            current = "formations"
        elif text.startswith("Langues"):
            current = "langues"
        elif "Compétences" in text:
            current = "competences"
        elif "Expériences" in text:
            current = "experiences"
        elif current:
            data[current].append(text)
    return data

if uploaded_file:
    doc_in = Document(uploaded_file)
    data = extract_data(doc_in)

    template = Document("Modèle_CV_SCC_2024.docx")

    for p in template.paragraphs:
        if "Prénom NOM" in p.text:
            p.text = "E. D."
        if "Technicien Support de Proximité" in p.text:
            p.text = "Technicien Systèmes et Réseaux"
        if "XX ans" in p.text:
            p.text = "30 ans d'expérience"

    template.add_page_break()
    template.add_paragraph("Données extraites du fichier source :", style="Heading 2")
    for section, items in data.items():
        template.add_paragraph(section.capitalize(), style="Heading 3")
        for i in items:
            template.add_paragraph(f"• {i}", style="List Bullet")

    buffer = BytesIO()
    template.save(buffer)
    buffer.seek(0)

    st.success("CV généré avec succès !")
    st.download_button("📥 Télécharger le CV SCC", buffer, file_name="CV_SCC_Généré.docx")
