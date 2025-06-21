import streamlit as st
import datetime
import pyperclip

st.set_page_config(page_title="Veo 3 Prompt Generator", layout="wide")

st.markdown(
    '''
    <div style="text-align: center;">
        <h1 style="font-size: 3em; color: #4A90E2;">🎬 Prompt Generator by Riki Oktopan</h1>
        <p style="font-size: 1.2em;">Buat prompt sinematik otomatis untuk Veo 3</p>
        <hr>
    </div>
    ''',
    unsafe_allow_html=True
)

camera_type = st.text_input("📸 Jenis Kamera", "8K cinematic camera")
camera_motion = st.text_input("🎥 Gerakan Kamera", "tracking shot, smooth motion")
lighting = st.text_input("💡 Pencahayaan", "golden hour, soft shadows")
style = st.text_input("🎨 Gaya Visual", "cyberpunk, hyperrealistic")
environment = st.text_input("🌆 Lokasi / Latar", "Tokyo city at night")
character = st.text_input("🧍 Tokoh / Karakter", "samurai with neon armor")
dialogue = st.text_area("🗣️ Narasi / Dialog (opsional)", "“This city never sleeps.”")
time_period = st.text_input("🕰️ Periode Waktu", "futuristic 2077")
weather = st.text_input("🌦️ Cuaca / Suasana", "rainy, neon reflections")
editing_style = st.text_input("✂️ Gaya Editing", "high contrast, fast cuts")

if st.button("🎬 Generate Prompt"):
    prompt_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    indo_prompt = f"""Menggunakan {camera_type} dengan {camera_motion}, menampilkan {character} di {environment} pada periode {time_period}. 
Suasana {weather}, pencahayaan {lighting}, dengan gaya visual {style}, dan gaya editing {editing_style}.
Narasi: {dialogue}"""

    eng_prompt = f"""Shot using a {camera_type} with {camera_motion}, featuring {character} in {environment} during the {time_period} era.
The mood is {weather}, lighting is {lighting}, visual style is {style}, editing style is {editing_style}.
Dialogue: {dialogue}"""

    st.subheader("🇮🇩 Prompt Indonesia (editable)")
    st.text_area("Prompt ID: " + prompt_id, value=indo_prompt, height=150)

    st.subheader("🇺🇸 Final Prompt (English)")
    st.code(eng_prompt, language='text')

    if st.button("📋 Copy English Prompt"):
        st.toast("📋 Prompt copied to clipboard!")
        pyperclip.copy(eng_prompt)
