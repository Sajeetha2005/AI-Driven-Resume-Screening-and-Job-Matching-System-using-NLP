import PyPDF2
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize NLP tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def extract_text_from_pdf(pdf_path):
    """
    Extracts raw text from a PDF resume
    """
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


def preprocess_text(text):
    """
    Cleans and preprocesses text using NLP techniques
    """
    # Convert to lowercase
    text = text.lower()

    # Remove numbers and punctuation
    text = re.sub(r'[^a-z\s]', ' ', text)

    # Tokenization
    tokens = nltk.word_tokenize(text)

    # Remove stopwords and lemmatize
    clean_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words and len(word) > 2
    ]

    return " ".join(clean_tokens)
