import random

# Step 1: Load sentences from the file
def load_sentences(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        sentences = file.readlines()  # Read all lines
    return [sentence.strip() for sentence in sentences if sentence.strip()]  # Remove empty lines

# Step 2: Introduce grammar errors into a sentence
def introduce_grammar_errors(sentence, error_rate=0.2):
    words = sentence.split()
    error_type = random.choice(["swap", "missing_particle", "extra_word"])  # Randomly choose an error type
    
    # Swap two words
    if error_type == "swap" and len(words) > 1:
        idx1, idx2 = random.sample(range(len(words)), 2)
        words[idx1], words[idx2] = words[idx2], words[idx1]
    
    # Remove particles (e.g., common Sinhala particles like "ට", "ේ", "ගෙන්")
    elif error_type == "missing_particle":
        particles_to_remove = ["ට", "ේ", "ගෙන්"]
        words = [word for word in words if word not in particles_to_remove]
    
    # Insert an extra word randomly
    elif error_type == "extra_word":
        extra_word = random.choice(["එක", "යන්න", "ගැන"])  # Common Sinhala extra words
        position = random.randint(0, len(words))
        words.insert(position, extra_word)
    
    return " ".join(words)

# Step 3: Process sentences with grammar errors
def process_sentences_with_grammar_errors(file_path, error_rate=0.2):
    sentences = load_sentences(file_path)  # Load sentences from the file
    modified_sentences = [introduce_grammar_errors(sentence, error_rate) for sentence in sentences]
    return modified_sentences

# Example Usage
file_path = "sentences.txt"
error_rate = 0.2  # Adjust the error rate as needed

# Load and process sentences with grammar errors
original_sentences = load_sentences(file_path)
modified_sentences = process_sentences_with_grammar_errors(file_path, error_rate)

# Print original and modified sentences
for original, modified in zip(original_sentences[:5], modified_sentences[:5]):  # Show first 5 sentences
    print(f"Original: {original}")
    print(f"With Grammar Errors: {modified}")
    print()
#save
output_file = "grammar_error.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for sentence in modified_sentences:
        file.write(sentence + "\n")