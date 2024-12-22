import pandas as pd

# File paths
sentences_path = "sentences.txt"
spelling_error_path = "spelling_error.txt"
grammar_error_path = "grammar_error.txt"

# Read content from files
with open(sentences_path, "r", encoding="utf-8") as f:
    sentences = f.readlines()

with open(spelling_error_path, "r", encoding="utf-8") as f:
    spelling_errors = f.readlines()

with open(grammar_error_path, "r", encoding="utf-8") as f:
    grammar_errors = f.readlines()

# Create a structured DataFrame
data = {
    "Original Sentence": [s.strip() for s in sentences],
    "Spelling Error": [s.strip() for s in spelling_errors],
    "Grammar Error": [s.strip() for s in grammar_errors]
}

df = pd.DataFrame(data)

# Save the structured dataset
output_path = "sinhala_dataset.csv"
df.to_csv(output_path, index=False, encoding="utf-8")

output_path
