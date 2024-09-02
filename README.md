# 🌎 TRANSLINGO 🔡

**Translingo** is a simple and intuitive text translation web application built with Streamlit. The app allows users to translate English text into various target languages using pre-trained models from the `transformers` library by Hugging Face.

## Features

- **User-Friendly Interface**: Clean and minimalistic design with a focus on ease of use.
- **Multiple Language Support**: Translate text from English to French, Spanish, German, Italian, and Urdu.
- **Real-time Translation**: Get instant translations by simply entering your text and selecting a target language.
- **Custom Styling**: The app features a gradient background with custom-styled text areas and output boxes for a polished user experience.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Translingo.git
   cd Translingo
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter the English text you want to translate in the input box.
2. Select the target language from the dropdown menu.
3. Click on the "Translate" button to see the translated text in the output box.

## Languages Supported

- **French** (`Helsinki-NLP/opus-mt-en-fr`)
- **Spanish** (`Helsinki-NLP/opus-mt-en-es`)
- **German** (`Helsinki-NLP/opus-mt-en-de`)
- **Italian** (`Helsinki-NLP/opus-mt-en-it`)
- **Urdu** (`Helsinki-NLP/opus-mt-en-ur`)

## Custom Styling

The app is styled with custom CSS to provide a seamless user experience:

- **Background**: Gradient from #ff7e5f to #feb47b
- **Title**: Light green background with rounded corners
- **Output Box**: White background with a border and rounded corners

## Demo

Check the Live demo of my project here: https://huggingface.co/spaces/Moezulhaq24/Translingo


## Acknowledgements

- Hugging Face's `transformers` library for providing the pre-trained models.
- Streamlit for creating an easy-to-use platform for deploying ML models.

 
