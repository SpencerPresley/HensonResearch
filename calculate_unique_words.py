# Description: This script calculates the number of unique characters and words in a dataset.
# Used in the Henson Research project to calculate the number of unique characters and words in the enwik8 dataset.
# Part of a series of scripts to determine token size and vocabulary size most appropriate for the dataset.

from collections import Counter
import re

def calculate_unique_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.lower().split()
    total_chars = len(text)
    unique_chars = len(set(text.lower()))
    total_words = len(words)
    unique_words = len(set(words))
    return total_chars, unique_chars, total_words, unique_words

# Define a function to read the file and count characters and words
def count_chars_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Count characters (including spaces and punctuation)
    char_counts = Counter(text)
    total_chars = sum(char_counts.values())
    
    # Count words by splitting on whitespace
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    
    return total_chars, len(char_counts), total_words, len(word_counts)

# Define a function to tokenize using a simple tokenizer and count tokens
def simple_tokenize_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize on spaces for a crude approximation of "words"
    tokens_space = text.split()
    
    # Tokenize based on word characters for a better approximation
    tokens_word = re.findall(r'\w+', text.lower())
    
    return len(tokens_space), len(set(tokens_space)), len(tokens_word), len(set(tokens_word))




if __name__ == "__main__":
    filename = 'enwik8.txt'
    total_chars, unique_chars, total_words, unique_words = calculate_unique_words(filename)
    print(f"Total characters in dataset: {total_chars}")
    print(f"Number of unique characters in dataset: {unique_chars}")
    print(f"Total words in dataset: {total_words}")
    print(f"Number of unique words in dataset: {unique_words}")
    print(f"Percentage of unique characters: {(unique_chars/total_chars)*100}%")
    print(f"Percentage of unique words: {(unique_words/total_words)*100}%\n\n")
    
    # Count characters and words
    total_chars, unique_chars, total_words, unique_words = count_chars_words(filename)
    print(f"Total characters: {total_chars}\nUnique characters: {unique_chars}\nTotal words: {total_words}\nUnique words: {unique_words}")

    # Tokenize and count again for comparison
    total_tokens_space, unique_tokens_space, total_tokens_word, unique_tokens_word = simple_tokenize_count(filename)
    print(f"Total tokens (space): {total_tokens_space}\nUnique tokens (space): {unique_tokens_space}\nTotal tokens (word): {total_tokens_word}\nUnique tokens (word): {unique_tokens_word}")

    #(total_chars, unique_chars, total_words, unique_words), (total_tokens_space, unique_tokens_space, total_tokens_word, unique_tokens_word)
    
