import os
import streamlit as st
from PIL import Image
from services.azure_di import read_text
from services.parser import extract_card_fields
from services.validator import luhn_check, detect_issuer
from services.utils import mask_card_number, format_date_display

st.set_page_config(page_title="Card Reader • Azure Document Intelligence", layout="centered")

endpoint = os.getenv("AZURE_FORMREC_ENDPOINT")
key = os.getenv("AZURE_FORMREC_KEY")

st.title("Leitor de Cartões • Azure Document Intelligence")
uploaded = st.file_uploader("Envie a imagem do cartão", type=["png","jpg","jpeg"])

if uploaded and endpoint and key:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, use_column_width=True)
    with st.spinner("Analisando com Azure AI Document Intelligence..."):
        full_text = read_text(endpoint, key, uploaded.read())
        fields = extract_card_fields(full_text)
    number = fields.get("number")
    name = fields.get("name")
    expiry = fields.get("expiry")
    issuer = detect_issuer(number) if number else None
    valid = luhn_check(number) if number else False
    st.subheader("Resultado")
    st.markdown(f"**Número (mascarado):** {mask_card_number(number) if number else 'não detectado'}")
    st.markdown(f"**Validação Luhn:** {'Válido' if valid else 'Inválido' if number else 'n/d'}")
    st.markdown(f"**Titular:** {name if name else 'não detectado'}")
    st.markdown(f"**Validade:** {format_date_display(expiry) if expiry else 'não detectado'}")
    st.markdown(f"**Emissor:** {issuer if issuer else 'não identificado'}")
elif uploaded and (not endpoint or not key):
    st.error("Defina AZURE_FORMREC_ENDPOINT e AZURE_FORMREC_KEY no ambiente.")
