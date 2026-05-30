import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import os

# ── Page config (must be first Streamlit call) ────────────────────────────────
st.set_page_config(
    page_title="NutriLens · Food AI",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #F7F3EE;
    color: #1C2B1E;
}
.stApp { background-color: #F7F3EE; }
#MainMenu, footer, header { visibility: hidden; }

.hero {
    background: linear-gradient(135deg, #1C3A22 0%, #2E5E38 60%, #4A8C56 100%);
    border-radius: 24px;
    padding: 52px 48px 44px;
    margin-bottom: 36px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(255,255,255,0.07) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem; font-weight: 900;
    color: #F7F3EE; line-height: 1.1;
    margin: 0 0 12px; letter-spacing: -0.5px;
}
.hero-sub {
    font-size: 1.05rem; font-weight: 300;
    color: rgba(247,243,238,0.75);
    max-width: 520px; line-height: 1.6; margin: 0;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25);
    color: #F7F3EE; font-size: 0.72rem; font-weight: 500;
    letter-spacing: 1.5px; text-transform: uppercase;
    padding: 6px 14px; border-radius: 50px; margin-bottom: 20px;
}
.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 1.55rem; font-weight: 700;
    color: #1C2B1E; margin: 0 0 6px;
}
.section-sub { font-size: 0.88rem; color: #6B7C6E; margin-bottom: 24px; }

.pred-card {
    background: linear-gradient(135deg, #1C3A22, #2E5E38);
    border-radius: 20px; padding: 32px 28px;
    color: #F7F3EE; text-align: center;
}
.pred-label {
    font-size: 0.72rem; letter-spacing: 2px;
    text-transform: uppercase; color: rgba(247,243,238,0.6); margin-bottom: 8px;
}
.pred-food {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem; font-weight: 900;
    color: #F7F3EE; margin: 0 0 4px; text-transform: capitalize;
}
.pred-conf { font-size: 0.9rem; color: rgba(247,243,238,0.7); margin-bottom: 20px; }
.conf-bar-bg {
    background: rgba(255,255,255,0.15); border-radius: 50px;
    height: 8px; margin: 0 auto; max-width: 200px; overflow: hidden;
}
.conf-bar-fill {
    height: 100%; border-radius: 50px;
    background: linear-gradient(90deg, #8BC99A, #F5E17A);
}

.calorie-card {
    background: #FFF8ED; border: 1.5px solid #F0D9A8;
    border-radius: 16px; padding: 24px 20px; text-align: center;
}
.calorie-number {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem; font-weight: 900;
    color: #C97D1E; line-height: 1; margin: 0;
}
.calorie-unit {
    font-size: 0.8rem; color: #A6884A;
    letter-spacing: 1px; text-transform: uppercase; margin-top: 4px;
}

.macro-row { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px; }
.macro-pill {
    flex: 1; min-width: 72px;
    background: #FFFFFF; border: 1.5px solid #E2EBE4;
    border-radius: 14px; padding: 12px 8px; text-align: center;
}
.macro-pill-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem; font-weight: 700;
    color: #1C3A22; display: block;
}
.macro-pill-label {
    font-size: 0.68rem; color: #6B7C6E;
    text-transform: uppercase; letter-spacing: 1px;
    display: block; margin-top: 2px;
}
.macro-pill-unit { font-size: 0.65rem; color: #9AA89C; }

.topn-row { margin-bottom: 10px; }
.topn-label {
    font-size: 0.82rem; color: #1C2B1E;
    text-transform: capitalize; margin-bottom: 3px;
    display: flex; justify-content: space-between;
}
.topn-bar-bg { background: #E8EDE9; border-radius: 50px; height: 9px; overflow: hidden; }
.topn-bar-fill {
    height: 100%; border-radius: 50px;
    background: linear-gradient(90deg, #2E5E38, #6BAD78);
}

.info-box {
    background: #EBF2EC; border-left: 4px solid #2E5E38;
    border-radius: 0 12px 12px 0; padding: 16px 20px;
    font-size: 0.87rem; color: #2E4A32; line-height: 1.6;
}
.tip-card {
    background: #FFFFFF; border-radius: 16px;
    padding: 22px 20px; border: 1.5px solid #E2EBE4; margin-bottom: 14px;
}
.tip-icon { font-size: 1.4rem; margin-bottom: 8px; }
.tip-title { font-weight: 500; font-size: 0.9rem; color: #1C3A22; margin-bottom: 4px; }
.tip-desc { font-size: 0.82rem; color: #6B7C6E; line-height: 1.5; }

.footer-line {
    text-align: center; font-size: 0.78rem; color: #9AA89C;
    padding: 28px 0 10px; letter-spacing: 0.5px;
}

div[data-testid="stFileUploader"] > div {
    background: #FFFFFF !important; border-radius: 16px !important;
    border: 2px dashed #C5D9C8 !important;
}
div[data-testid="stFileUploader"] > div:hover { border-color: #2E5E38 !important; }
.stButton > button {
    background: linear-gradient(135deg, #1C3A22, #2E5E38) !important;
    color: #F7F3EE !important; border: none !important;
    border-radius: 50px !important; padding: 12px 36px !important;
    font-family: 'DM Sans', sans-serif !important; font-weight: 500 !important;
    font-size: 0.95rem !important; width: 100% !important;
}
.stButton > button:hover { opacity: 0.88 !important; }
</style>
""", unsafe_allow_html=True)


# ── Model loader — supports both .keras and .h5 ───────────────────────────────
@st.cache_resource(show_spinner="Loading AI model…")
def load_model():
    import tensorflow as tf
    for model_path in ["food11_model.keras", "food11_model.h5"]:
        if os.path.exists(model_path):
            try:
                model = tf.keras.models.load_model(model_path)
                return model, None, model_path
            except Exception as e:
                return None, str(e), model_path
    return None, "No model file found. Place food11_model.keras (or food11_model.h5) next to app.py.", ""


# ── Nutrition loader — reads your exact CSV columns ───────────────────────────
@st.cache_data
def load_nutrition(csv_path="food11_calories_full.csv"):
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        # Normalise class names for case-insensitive lookup
        df["class_name"] = df["class_name"].str.strip()
        return df
    # Fallback using your exact CSV values
    data = {
        "class_name":       ["Bread","Dairy product","Dessert","Egg",
                              "Fried food","Meat","Noodles/Pasta","Rice",
                              "Seafood","Soup","Vegetable/Fruit"],
        "calories":         [265, 150, 350, 155, 320, 250, 220, 130, 200, 120,  80],
        "carbs_g":          [49,   12,  50,  1.1, 28,   0,  43,  28,   5,  15,  18],
        "protein_g":        [9,     8,   5,  13,   7,  26,   8,  2.7, 22,   4,   2],
        "fat_g":            [3.2,   8,  15,  11,  20,  15,   2,  0.3, 10,   4, 0.5],
        "fiber_g":          [2.7,   0, 1.5,   0,   2,   0, 2.5,  0.4,  0, 1.5,   4],
        "sugar_g":          [5,    11,  35, 1.1, 1.5,   0,   2,  0.1,  0,   3,  10],
        "sodium_mg":        [491,  105, 250, 124, 450,  72, 180,    1, 150, 500,  30],
        "cholesterol_mg":   [0,    30,  45, 373,  40,  90,   0,    0,  70,  10,   0],
    }
    return pd.DataFrame(data)


# ── Constants ─────────────────────────────────────────────────────────────────
# ── Confirmed class_indices (from model training) ────────────────────────────
# Exactly as returned by flow_from_directory on the Food-11 dataset:
# {'Bread':0,'Dairy product':1,'Dessert':2,'Egg':3,'Fried food':4,
#  'Meat':5,'Noodles-Pasta':6,'Rice':7,'Seafood':8,'Soup':9,'Vegetable-Fruit':10}
CLASS_NAMES = [
    "Bread",           # 0
    "Dairy product",   # 1
    "Dessert",         # 2
    "Egg",             # 3
    "Fried food",      # 4
    "Meat",            # 5
    "Noodles-Pasta",   # 6
    "Rice",            # 7
    "Seafood",         # 8
    "Soup",            # 9
    "Vegetable-Fruit", # 10
]

# Display-friendly names for UI
_LABEL_DISPLAY = {
    "Noodles-Pasta":   "Noodles / Pasta",
    "Vegetable-Fruit": "Vegetable / Fruit",
}

CLASS_EMOJI = {
    "Bread": "🍞", "Dairy product": "🧀", "Dessert": "🍰", "Egg": "🥚",
    "Fried food": "🍟", "Meat": "🥩", "Noodles-Pasta": "🍝", "Rice": "🍚",
    "Seafood": "🦐", "Soup": "🍲", "Vegetable-Fruit": "🥦",
}


# ── Helpers ───────────────────────────────────────────────────────────────────
def preprocess_image(img: Image.Image) -> "np.ndarray":
    from tensorflow.keras.applications.efficientnet import preprocess_input
    img = img.convert("RGB").resize((224, 224))
    arr = np.array(img, dtype=np.float32)
    arr = np.expand_dims(arr, axis=0)
    return preprocess_input(arr)


def predict(model, img: Image.Image):
    inp = preprocess_image(img)
    probs = model.predict(inp, verbose=0)[0]
    idx = int(np.argmax(probs))
    return CLASS_NAMES[idx], float(probs[idx]), probs


def get_nutrition(df: pd.DataFrame, food_name: str):
    # Normalise dashes to slashes so "Noodles-Pasta" matches CSV "Noodles/Pasta"
    lookup = food_name.replace("-", "/")
    row = df[df["class_name"].str.lower() == lookup.lower()]
    return row.iloc[0] if not row.empty else None

def display_name(food_name: str) -> str:
    """Return pretty UI name (dash -> slash for display)."""
    return _LABEL_DISPLAY.get(food_name, food_name)


def macro_pill(value, label, unit):
    return f"""<div class="macro-pill">
        <span class="macro-pill-value">{value}</span>
        <span class="macro-pill-label">{label}</span>
        <span class="macro-pill-unit">{unit}</span>
    </div>"""


def topn_bar(label, prob, max_prob):
    pct = int(prob / max_prob * 100) if max_prob > 0 else 0
    dlabel = _LABEL_DISPLAY.get(label, label)
    return f"""<div class="topn-row">
        <div class="topn-label">
            <span>{CLASS_EMOJI.get(label,'')} {dlabel}</span>
            <span style="color:#6B7C6E">{prob*100:.1f}%</span>
        </div>
        <div class="topn-bar-bg">
            <div class="topn-bar-fill" style="width:{pct}%"></div>
        </div>
    </div>"""


# ── Sidebar: live class-index debug panel ─────────────────────────────────────
with st.sidebar:
    st.markdown("### 🗂️ Live Class Index Map")
    st.caption("This shows the exact order your model uses. If a label looks wrong, check your training class_indices.")
    if 'CLASS_NAMES' in dir():
        for i, name in enumerate(CLASS_NAMES):
            st.markdown(f"`[{i}]` {name}")
    else:
        st.info("Load the model to see class mapping.")

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">🌿 AI · Nutrition · Vision</div>
  <div class="hero-title">NutriLens</div>
  <p class="hero-sub">
      Snap a photo of any meal. Our EfficientNetB0 model identifies the food
      and delivers an instant full nutrition breakdown — calories, macros, and more.
  </p>
</div>
""", unsafe_allow_html=True)

# ── Load assets ───────────────────────────────────────────────────────────────
model, model_err, model_path = load_model()
nutrition_df = load_nutrition()

# ── Layout ────────────────────────────────────────────────────────────────────
left, right = st.columns([1, 1.3], gap="large")

with left:
    st.markdown('<div class="section-heading">Upload Food Image</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">JPG, PNG, WEBP — clear top-down or front view works best</div>', unsafe_allow_html=True)

    uploaded = st.file_uploader("", type=["jpg", "jpeg", "png", "webp"], label_visibility="collapsed")

    if uploaded:
        img = Image.open(uploaded)
        st.image(img, use_container_width=True, caption="")
        run_btn = st.button("🔍  Analyse This Food")
    else:
        run_btn = False
        st.markdown("""
        <div style="text-align:center;padding:40px 0;color:#9AA89C;">
            <div style="font-size:3rem">📷</div>
            <div style="font-size:0.88rem;margin-top:8px">No image uploaded yet</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="tip-card">
        <div class="tip-icon">💡</div>
        <div class="tip-title">Best results</div>
        <div class="tip-desc">Use well-lit images with the food centred. Avoid blurry or obscured shots for highest accuracy.</div>
    </div>
    <div class="tip-card">
        <div class="tip-icon">🍽️</div>
        <div class="tip-title">Supported categories</div>
        <div class="tip-desc">Bread · Dairy · Dessert · Egg · Fried food · Meat · Noodles/Pasta · Rice · Seafood · Soup · Vegetable/Fruit</div>
    </div>
    """, unsafe_allow_html=True)


with right:
    st.markdown('<div class="section-heading">Prediction & Nutrition</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Results appear here after analysis</div>', unsafe_allow_html=True)

    if model_err:
        st.markdown(f"""
        <div class="info-box">
            ⚠️ <strong>Model not loaded.</strong>
            Place <code>food11_model.keras</code> in the same folder as <code>app.py</code>.<br><br>
            <em>{model_err}</em>
        </div>""", unsafe_allow_html=True)

    if uploaded and run_btn:
        if model is None:
            st.error("Model unavailable — see the note above.")
        else:
            with st.spinner("Classifying image…"):
                food_name, confidence, probs = predict(model, img)

            emoji    = CLASS_EMOJI.get(food_name, "🍽️")
            conf_pct = int(confidence * 100)

            # ── Prediction card ──
            st.markdown(f"""
            <div class="pred-card">
                <div class="pred-label">Detected food</div>
                <div class="pred-food">{emoji} {display_name(food_name)}</div>
                <div class="pred-conf">Model confidence: {conf_pct}%</div>
                <div class="conf-bar-bg">
                    <div class="conf-bar-fill" style="width:{conf_pct}%"></div>
                </div>
            </div>""", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # ── Nutrition ──
            ninfo = get_nutrition(nutrition_df, food_name)
            if ninfo is not None:
                cal = ninfo["calories"]

                # Calorie spotlight
                st.markdown(f"""
                <div class="calorie-card">
                    <div class="calorie-unit">Estimated Calories</div>
                    <div class="calorie-number">{int(cal)}</div>
                    <div class="calorie-unit" style="margin-top:4px">kcal per 100 g</div>
                </div>""", unsafe_allow_html=True)

                # 8 macro pills (includes cholesterol from your CSV)
                pills = '<div class="macro-row">'
                pills += macro_pill(f"{ninfo['carbs_g']:.1f}",    "Carbs",   "g")
                pills += macro_pill(f"{ninfo['protein_g']:.1f}",  "Protein", "g")
                pills += macro_pill(f"{ninfo['fat_g']:.1f}",      "Fat",     "g")
                pills += macro_pill(f"{ninfo['fiber_g']:.1f}",    "Fiber",   "g")
                pills += macro_pill(f"{ninfo['sugar_g']:.1f}",    "Sugar",   "g")
                pills += macro_pill(f"{int(ninfo['sodium_mg'])}",  "Sodium",  "mg")
                pills += macro_pill(f"{int(ninfo['cholesterol_mg'])}", "Cholest.", "mg")
                pills += '</div>'
                st.markdown(pills, unsafe_allow_html=True)

                # Daily Value % expander
                st.markdown("<br>", unsafe_allow_html=True)
                with st.expander("📊  Daily Value % (based on 2000 kcal diet)", expanded=False):
                    daily_refs = {
                        "Calories":       (cal,                    2000, "kcal"),
                        "Carbohydrates":  (ninfo["carbs_g"],        300,  "g"),
                        "Protein":        (ninfo["protein_g"],       50,  "g"),
                        "Fat":            (ninfo["fat_g"],            65,  "g"),
                        "Fiber":          (ninfo["fiber_g"],          25,  "g"),
                        "Sugar":          (ninfo["sugar_g"],          50,  "g"),
                        "Sodium":         (ninfo["sodium_mg"],      2300, "mg"),
                        "Cholesterol":    (ninfo["cholesterol_mg"],  300, "mg"),
                    }
                    for nutrient, (val, ref, unit) in daily_refs.items():
                        pct = min(float(val) / ref, 1.0)
                        st.write(f"**{nutrient}** — {val:.1f} {unit}  ({pct*100:.0f}% DV)")
                        st.progress(pct)

            else:
                st.markdown("""
                <div class="info-box">
                    Nutrition data not found for this class. Check that
                    <code>food11_calories_full.csv</code> is in the same folder as
                    <code>app.py</code> and the <code>class_name</code> column
                    matches the Food-11 folder names exactly.
                </div>""", unsafe_allow_html=True)

            # ── Top-5 predictions ──
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("**Top 5 Predictions**")
            top5_idx = np.argsort(probs)[::-1][:5]
            top5     = [(CLASS_NAMES[i], float(probs[i])) for i in top5_idx]
            max_p    = top5[0][1]
            bars     = "".join(topn_bar(lbl, p, max_p) for lbl, p in top5)
            st.markdown(bars, unsafe_allow_html=True)

    elif not uploaded:
        st.markdown("""
        <div style="background:#FFFFFF;border-radius:20px;padding:60px 32px;
                    text-align:center;border:1.5px solid #E2EBE4;">
            <div style="font-size:3.5rem;margin-bottom:16px">🤖</div>
            <div style="font-family:'Playfair Display',serif;font-size:1.3rem;
                        color:#1C2B1E;margin-bottom:8px">Awaiting your photo</div>
            <div style="font-size:0.88rem;color:#9AA89C;max-width:300px;
                        margin:0 auto;line-height:1.6">
                Upload a food image on the left to receive an instant
                AI-powered classification and full nutrition report.
            </div>
        </div>""", unsafe_allow_html=True)

# ── Model info strip ──────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
loaded_name = os.path.basename(model_path) if model_path else "—"
c1, c2, c3, c4 = st.columns(4)
for col, icon, label, value in zip(
    [c1, c2, c3, c4],
    ["🧠",             "📦",                "🗂️",               "⚡"],
    ["Architecture",   "Dataset",           "Classes",          "Model file"],
    ["EfficientNetB0", "Food-11 (~16k imgs)","11 food categories", loaded_name],
):
    with col:
        st.markdown(f"""
        <div style="background:#FFFFFF;border-radius:14px;padding:18px 16px;
                    border:1.5px solid #E2EBE4;text-align:center;">
            <div style="font-size:1.5rem">{icon}</div>
            <div style="font-size:0.72rem;color:#6B7C6E;text-transform:uppercase;
                        letter-spacing:1px;margin:4px 0 2px">{label}</div>
            <div style="font-size:0.88rem;font-weight:500;color:#1C2B1E">{value}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-line">
    NutriLens · EfficientNetB0 + Streamlit · Food-11 Dataset
</div>""", unsafe_allow_html=True)