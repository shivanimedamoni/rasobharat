# REPORT.md

##  Application Overview
*Amma Cheti Vontalu* (RasoBharat) is a Telugu-first recipe generation application that provides step-by-step cooking instructions, inspired by traditional Indian kitchens.  

### Key Features:
- Select *Ingredients, Tools, Extra Items, and Time* before generating a recipe.
- AI-powered *Recipe Generator* (using Google Gemini API).
- Telugu-first UI with smooth navigation like "Katalu → Vontakalu".
- Accessible via a *public Streamlit app* for real-time usage.

*MVP Scope*:
- Ingredient input by users.
- Recipe generation with AI model.
- Basic UI navigation (Ingredients → Tools → Time → Recipe).
- Deployment on *Streamlit Cloud* (linked to Hugging Face/GitHub).

---

##  AI Integration Details
- *Model Used*: Google Gemini 1.5 Flash (Generative AI).
- *API Key Management*: Stored securely in secrets.toml (not exposed in repo).
- *Workflow*:
  1. User selects ingredients/tools.
  2. Prompt is dynamically generated.
  3. Gemini API generates recipe in Telugu/English.
  4. Recipe is displayed with cooking steps.

---

##  Technical Architecture & Development
### Tech Stack:
- *Frontend/UI*: Streamlit
- *Backend*: Python 3.10+
- *AI API*: Google Gemini (via google-generativeai library)
- *Deployment*: Streamlit Cloud (Live Demo), GitHub for version control, Swecha GitLab for submission.

### File Structure:
rasobharat/
│── app.py
│── requirements.txt
│── README.md
│── REPORT.md
│── CONTRIBUTING.md
│── CHANGELOG.md
│── LICENSE
│── .gitignore

### Development Highlights:
- Modular Python code for recipe generation.
- Used .gitignore to hide sensitive files.
- Clear documentation (README.md) for easy setup.

---

##  User Testing & Feedback
### Methodology:
- Conducted *Week 2 testing* with a small group of peers.
- Tested navigation (Ingredients → Tools → Recipe Generator).
- Checked AI outputs for clarity and cultural authenticity.

### Feedback Summary:
- *Positive*: Easy navigation, authentic recipe results, Telugu support appreciated.
- *Improvements Suggested*:
  - Add option for multiple recipes per ingredient set.
  - Include cooking time estimation.
  - Provide images alongside text recipes.

---

##  Future Enhancements
- Support for multiple Indian languages.
- Save & share recipe option.
- AI-powered *nutrition calculator*.
- Voice-based interaction for elderly users.

---

## 7. References
- [Google Gemini API Documentation](https://ai.google.dev/)
- [Swecha GitLab](https://code.swecha.org/)

---

## 8. Live Application Link
👉 [RasoBharat – Live Demo](https://a3zabek2hajlvsofxcdpsd.streamlit.app/)
