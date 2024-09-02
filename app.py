import streamlit as st
from transformers import pipeline

# Define model mapping for each target language
model_mapping = {
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Italian": "Helsinki-NLP/opus-mt-en-it",
    "Urdu": "Helsinki-NLP/opus-mt-en-ur"  # Added Urdu translation
}


st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        height: 100vh;
        padding: 2rem;
    }
    .block-container {
        padding: 2rem;
    }
    .title {
        background-color: #d4edda;  /* Light green color */
        padding: 1rem;
        border-radius: 8px;
        text-align: left;
        margin-bottom: 1rem;
    }
    .output-box {
        background-color: #ffffff;  
        border: 1px solid #ccc;    
        border-radius: 8px;       
        padding: 1rem;
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="title">🌎 TRANSLINGO 🔡</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

# Center the content in the middle column
with col2:
    st.header("Translate Text")
    
    # Input text
    text = st.text_area("Enter text in English:")
    
    # Target language selection
    selected_language = st.selectbox("Select target language:", list(model_mapping.keys()))
    
    # Translation button
    if st.button("Translate"):
        if text:
            # Get the appropriate model based on selected language
            model_name = model_mapping[selected_language]
            translator = pipeline("translation", model=model_name)
            
            # Perform translation
            translation = translator(text, max_length=400)[0]['translation_text']
            
            # Display translation
            st.markdown(
                f'<div class="output-box"><h3>Translation in {selected_language}:</h3><p>{translation}</p></div>',
                unsafe_allow_html=True
            )
        else:
            st.write("Please enter some text to translate.")
