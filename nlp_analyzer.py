import re
from collections import Counter

def count_specific_word(text, search_word):
    # Convert both text and search_word to lowercase for case-insensitive counting
    text_lower = text.lower()
    search_word_lower = search_word.lower()
    
    if not search_word_lower:
        return 0

    # Use a while loop to count occurrences
    count = 0
    start_index = 0
    while True:
        index = text_lower.find(search_word_lower, start_index)
        if index == -1:
            break
        count += 1
        start_index = index + len(search_word_lower)
    return count

def identify_most_common_word(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    words = cleaned_text.split()
    
    if not words:
        return None

    # Use Counter to find word frequencies
    word_counts = Counter(words)
    
    # Find the most common word
    most_common = word_counts.most_common(1)
    if most_common:
        return most_common[0][0]
    return None

def calculate_average_word_length(text):
    # Remove punctuation and split into words
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.split()
    
    if not words:
        return 0.0

    total_length = 0
    # Use a for loop to sum word lengths
    for word in words:
        total_length += len(word)
    
    average_length = total_length / len(words)
    return float(f"{average_length:.2f}") # Format to two decimal places

def count_paragraphs(text):
    # Paragraphs are typically separated by two or more newline characters
    # or by a single newline if the previous line was empty.
    # We'll split by two or more newlines and filter out empty strings.
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n+', text) if p.strip()]
    return len(paragraphs)

def count_sentences(text):
    # Sentences typically end with '.', '!', '?' followed by whitespace or end of string
    # Use regex to find sentence endings. This is a basic approach and might not cover all edge cases.
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Filter out any empty strings that might result from splitting
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

# Example Usage (demonstrating if/else)
if __name__ == "__main__":
    sample_article = """
    This is the first paragraph of a sample news article. It contains several sentences.
    For example, this is one sentence! And this is another. Is this clear?

    This is the second paragraph. It has fewer sentences.
    The word 'sentence' appears multiple times. The word 'paragraph' also appears.
    """

    print(f"Specific word 'sentence' count: {count_specific_word(sample_article, 'sentence')}")
    print(f"Most common word: {identify_most_common_word(sample_article)}")
    print(f"Average word length: {calculate_average_word_length(sample_article)}")
    print(f"Paragraph count: {count_paragraphs(sample_article)}")
    print(f"Sentence count: {count_sentences(sample_article)}")

    # Demonstrating if/else with a condition
    if count_paragraphs(sample_article) > 1:
        print("The article has more than one paragraph.")
    else:
        print("The article has one or no paragraphs.")
