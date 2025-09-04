import streamlit as st
import google.generativeai as genai

# 🔑 API Key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Page Config
st.set_page_config(page_title="అమ్మ చేతి వంట", page_icon="🍲", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    body {
        background-color: #1c1c1c;
        color: white;
    }
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #4CAF50;
        margin-bottom: 8px;
    }
    .subtitle {
        text-align: center;
        font-size: 40px;
        color: #ddd;
        margin-bottom: 30px;
    }
    .menu-buttons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
    }
    .menu-buttons a {
        font-size: 30px;
        font-weight: bold;
        padding: 12px 32px;
        border-radius: 12px;
        background: linear-gradient(90deg, #28a745, #6bcf63);
        color: white;
        text-decoration: none;
    }
    .menu-buttons a:hover {
        background: linear-gradient(90deg, #ffcc00, #ff6600);
        color: black;
    }
    .stButton>button {
        font-size: 24px !important;
        font-weight: bold !important;
        padding: 12px 32px;
        border-radius: 12px;
        background: linear-gradient(90deg, #28a745, #6bcf63);
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<div class='main-title'>🍲 అమ్మ చేతి వంట 🍲</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>మీ దగ్గర ఉన్న పదార్థాలతో రుచికరమైన వంటకాలు సులభంగా తయారు చేసుకోండి</div>", unsafe_allow_html=True)

# ---------- Menu Bar ----------
st.markdown("""
<div class='menu-buttons'>
    <a href="#home">🏠 హోమ్</a>
    <a href="#ingredients">🥕 పదార్థాలు</a>
    <a href="#tools">🥘 సామగ్రి</a>
    <a href="#extra">🍽 అదనపు పదార్థాలు</a>
    <a href="#time">⏰ సమయం</a>
    <a href="#generator">🤖 వంటకం తయారీ</a>
</div>
""", unsafe_allow_html=True)

# ---------- Sections ----------
# Home
st.markdown('<a name="home"></a>', unsafe_allow_html=True)
st.header("🏠 హోమ్")
st.write("ఇక్కడ మీరు మీ దగ్గర ఉన్న పదార్థాలతో వంటకాలు సులభంగా తయారు చేసుకోగలరు.")

# Ingredients
st.markdown('<a name="ingredients"></a>', unsafe_allow_html=True)
st.header("🥕 పదార్థాలు")
ingredients = st.multiselect("మీ వద్ద ఉన్న పదార్థాలను ఎంచుకోండి:",
    ["టమోటా", "ఉల్లి", "బంగాళదుంప", "పాలకూర", "గుడ్డు", "చికెన్", "పప్పు", "మిర్చి"],
    placeholder="🍅 ఒక పదార్థం ఎంచుకోండి...")

# Tools
st.markdown('<a name="tools"></a>', unsafe_allow_html=True)
st.header("🥘 వంట సామగ్రి")
tools = st.multiselect("మీ వద్ద ఉన్న వంట సామగ్రి:",
    ["ప్రెషర్ కుక్కర్", "పాన్", "కడాయి", "ఓవెన్", "ఫ్రైయింగ్ పాన్"],
    placeholder="🥄 ఒక వంట సామాను ఎంచుకోండి...")

# Extra Items
st.markdown('<a name="extra"></a>', unsafe_allow_html=True)
st.header("🍽 అదనపు పదార్థాలు")
new_ing = st.text_input("📝 కొత్త పదార్థం నమోదు చేయండి:", placeholder="ఉదా: బియ్యం, పప్పు...")

# Time
st.markdown('<a name="time"></a>', unsafe_allow_html=True)
st.header("⏰ వంట సమయం")
time = st.slider("వంట సమయం (నిమిషాలు)", 5, 120, 30)

# Recipe Generator
st.markdown('<a name="generator"></a>', unsafe_allow_html=True)
st.header("🤖 వంటకం తయారీ")

if st.button("🍛 రుచికరమైన వంటకం తయారు చేయండి 🍛", use_container_width=True):
    with st.spinner("వంటకం తయారవుతోంది..."):
        prompt = f"""
        నాకు ఈ పదార్థాలు ఉన్నాయి: {", ".join(ingredients)}.
        నేను వాడగల సామగ్రి: {", ".join(tools)}.
        నేను జోడించదలచిన అదనపు పదార్థం: {new_ing}.
        నాకు {time} నిమిషాల సమయం ఉంది.
        దయచేసి ఒక సులభమైన తెలుగు రెసిపీ ఇవ్వండి.
        """
        try:
            model=genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
                
            
            recipe = response.text
            st.success("🥗 మీ రెసిపీ సిద్ధం అయ్యింది!")
            st.write(recipe)
        except Exception as e:
            st.error(f"Error: {e}")