import random

# Step 1: Load sentences from the file
def load_sentences(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        sentences = file.readlines()  # Read all lines
    return [sentence.strip() for sentence in sentences if sentence.strip()]  # Remove extra spaces and empty lines

# Step 2: Introduce spelling errors into a word
def introduce_typo(word):
    if len(word) < 2:
        return word  # Skip very short words
    idx = random.randint(0, len(word) - 2)  # Randomly choose a position
    return word[:idx] + word[idx + 1] + word[idx] + word[idx + 2:]  # Swap two adjacent characters

# Step 3: Introduce spelling errors into a sentence
def introduce_spelling_errors(sentence, error_rate=0.3):
    words = sentence.split()
    num_errors = int(len(words) * error_rate)  # Number of words to introduce errors in
    for _ in range(num_errors):
        idx = random.randint(0, len(words) - 1)  # Randomly pick a word index
        words[idx] = introduce_typo(words[idx])  # Introduce a typo in the word
    return " ".join(words)

# Step 4: Process sentences
def process_sentences(file_path, error_rate=0.3):
    sentences = load_sentences(file_path)  # Load sentences from the file
    modified_sentences = [introduce_spelling_errors(sentence, error_rate) for sentence in sentences]
    return modified_sentences

# Example Usage
file_path = "sentences.txt"
error_rate = 0.3  # Adjust the error rate as needed

# Load and process sentences
original_sentences = load_sentences(file_path)
modified_sentences = process_sentences(file_path, error_rate)

# Print original and modified sentences
for original, modified in zip(original_sentences[:5], modified_sentences[:5]):  # Show the first 5 sentences
    print(f"Original: {original}")
    print(f"Modified: {modified}")

# Save the modified sentences to a file
output_file = "spelling_error.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for sentence in modified_sentences:
        file.write(sentence + "\n")
