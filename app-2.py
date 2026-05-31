import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Proyecto Umbral",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Ocultar chrome de Streamlit completamente ────────────────────────────────
st.markdown(
    """
    <style>
    /* Ocultar todo el chrome de Streamlit */
    #MainMenu, header, footer,
    [data-testid="stToolbar"],
    [data-testid="stHeader"],
    [data-testid="stSidebar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] { display: none !important; }

    /* Sin padding en el contenedor principal */
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stMain"] > div { padding: 0 !important; }
    html, body, [data-testid="stAppViewContainer"] {
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        background: #08080C !important;
    }
    /* Iframe ocupa toda la ventana */
    iframe { display: block; border: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Cargar el HTML ────────────────────────────────────────────────────────────
HTML_FILE = Path(__file__).parent / "proyecto-umbral.html"

if HTML_FILE.exists():
    html_content = HTML_FILE.read_text(encoding="utf-8")
else:
    st.error(
        "⚠️ No se encontró el archivo **proyecto-umbral.html** en el mismo directorio que app.py.\n\n"
        "Asegúrate de que ambos archivos estén juntos en el repositorio."
    )
    st.stop()

# ── Renderizar la experiencia completa ───────────────────────────────────────
# height=0 + scrolling=False hace que el iframe tome el 100vh del navegador
components.html(html_content, height=800, scrolling=True)
