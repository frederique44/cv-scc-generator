import streamlit as st
from utils.extractors import extract_text
from utils.parsers import parse_cv_data
from utils.generators import generate_scc_document
import base64

# Config
st.set_page_config(
    page_title="CV SCC Generator 2024",
    page_icon="📄",
    layout="centered"
)

# CSS personnalisé
st.markdown("""
<style>
.upload-area {
    border: 2px dashed #ccc;
    padding: 20px;
    text-align: center;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Interface
st.title("🔄 CV SCC Generator")
st.markdown("Transformez vos CV bruts en documents standardisés SCC 2024")

# Zone d'upload
with st.container():
    st.markdown('<div class="upload-area">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Déposez votre CV (PDF ou Word)",
        type=["pdf", "docx"],
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Traitement
if uploaded_file:
    with st.spinner("Analyse du CV en cours..."):
        try:
            # Extraction
            raw_text = extract_text(uploaded_file)
            
            # Parsing
            cv_data = parse_cv_data(raw_text)
            
            # Génération
            doc_bytes = generate_scc_document(cv_data)
            
            # Téléchargement
            st.success("CV converti avec succès !")
            st.download_button(
                label="⬇️ Télécharger le CV formaté",
                data=doc_bytes,
                file_name="CV_SCC_2024.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            
        except Exception as e:
            st.error(f"Erreur : {str(e)}")
            st.info("Assurez-vous que le CV contient une structure lisible.")
