import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

st.set_page_config(
    page_title="Concierge da Cabana Dreams",
    page_icon="🌿"
)

st.title("🌿 Concierge da Cabana Dreams")
st.caption("Assistente da cabana para tirar dúvidas da estadia.")
