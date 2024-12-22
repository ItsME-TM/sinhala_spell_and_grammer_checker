# Step 1: Load the raw text file
def load_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

# Step 2: Clean the text
import re

def clean_text(raw_text):
    # Remove unnecessary symbols, numbers, and English content, except periods
    cleaned_text = re.sub(r'[a-zA-Z0-9]', '', raw_text)  # Remove English letters and numbers
    cleaned_text = re.sub(r'[^\u0D80-\u0DFF\s.]', '', cleaned_text)  # Remove non-Sinhala symbols except periods
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Remove extra spaces
    return cleaned_text.strip()

# Example Usage
raw_text = load_text_file("news_text_file.txt")
cleaned_text = clean_text(raw_text)
print(cleaned_text[:500])  # Preview first 500 characters

def split_into_sentences(cleaned_text):
    # Split text into sentences using Sinhala-specific punctuation
    sentences = re.split(r'[.!?]', cleaned_text)
    # Remove empty sentences and extra whitespace
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences

# Example Usage
sentences = split_into_sentences(cleaned_text)
print(sentences[:5])  # Preview first 5 sentences

#save the sentences to a file
with open("sentences.txt", "w", encoding="utf-8") as file:
    for sentence in sentences:
        file.write(sentence + "\n")
