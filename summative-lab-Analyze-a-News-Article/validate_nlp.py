import pytest
from nlp_analyzer import count_specific_word, identify_most_common_word, calculate_average_word_length, count_paragraphs, count_sentences

def test_count_specific_word():
    text = "The quick brown fox jumps over the lazy dog. The dog was not happy.\n\nThis is a new paragraph."
    # Substring match "the" should find 3 (The, the, The)
    assert count_specific_word(text, "the") == 3
    # Empty search word should return 0
    assert count_specific_word(text, "") == 0

def test_identify_most_common_word():
    text = "The quick brown fox jumps over the lazy dog. The dog was not happy.\n\nThis is a new paragraph."
    # "the" appears 3 times, "dog" 2 times.
    assert identify_most_common_word(text) == "the"

def test_calculate_average_word_length():
    text = "The quick brown fox jumps over the lazy dog. The dog was not happy.\n\nThis is a new paragraph."
    # Avg: 71 / 19 = 3.7368... -> 3.74
    assert calculate_average_word_length(text) == 3.74

def test_count_paragraphs():
    text = "The quick brown fox jumps over the lazy dog. The dog was not happy.\n\nThis is a new paragraph."
    # Two paragraphs separated by \n\n
    assert count_paragraphs(text) == 2

def test_count_sentences():
    text = "The quick brown fox jumps over the lazy dog. The dog was not happy.\n\nThis is a new paragraph."
    # Sentences: 3
    assert count_sentences(text) == 3

if __name__ == "__main__":
    # If run as a script, just run the tests manually
    test_count_specific_word()
    test_identify_most_common_word()
    test_calculate_average_word_length()
    test_count_paragraphs()
    test_count_sentences()
    print("All tests passed!")
