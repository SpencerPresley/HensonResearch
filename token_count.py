import torch
from transformers import AutoTokenizer

# Load tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to read the file and tokenize in chunks
def count_tokens_in_file(file_path, chunk_size=100000):
    total_tokens = 0
    unique_tokens = set()
    
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            text = file.read(chunk_size)
            if not text:
                break  # End of file
            inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
            token_ids = inputs["input_ids"].tolist()[0]
            total_tokens += len(token_ids)
            unique_tokens.update(token_ids)
    
    return total_tokens, len(unique_tokens)

# Adjust the file path as necessary
file_path = 'enwik8.txt'
total_tokens, unique_token_count = count_tokens_in_file(file_path)

print(f"Total tokens: {total_tokens}")
print(f"Unique tokens: {unique_token_count}")