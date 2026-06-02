import re
from collections import Counter

# Load the news article content into a string variable
news_article = """ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the “Apple Pie Master,” this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. “This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results,” Doe explained.

Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, “The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one.”

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. “We want to cater to all taste preferences, from the traditional to the adventurous,” said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master’s environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. “Sustainability is at the core of all our product designs,” emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, “It’s like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings.”

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. “The Apple Pie Master is just the beginning,” said CEO Jane Doe. “We’re exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking.”

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations."""

def count_specific_word(text_to_search, search_word):
    """Counts the number of occurrences of search_word in text_to_search."""
    if not search_word:
        return 0

    text_lower = text_to_search.lower()
    word_lower = search_word.lower()
    count = 0
    index = 0

    # Use of WHILE LOOP as per criteria
    while True:
        index = text_lower.find(word_lower, index)
        if index == -1:
            break
        count += 1
        index += len(word_lower)
    return count


def identify_most_common_word(text):
    """Identifies the most common word in the text. Edge case: empty string returns None."""
    if not text.strip():
        return None

    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    words = cleaned_text.split()

    if not words:
        return None

    counts = Counter(words)
    return counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    """Calculates avg word length excluding punctuation. Edge case: empty string returns 0.0."""
    if not text.strip():
        return 0.0

    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.split()

    if not words:
        return 0.0

    total_chars = 0
    # Use of FOR LOOP as per criteria
    for word in words:
        total_chars += len(word)

    return round(float(total_chars / len(words)), 2)
def count_paragraphs(text):
    """Counts paragraphs based on empty lines. Edge case: empty string returns 1."""
    if not text.strip():
        return 1

    paragraphs = [p for p in re.split(r'\n\s*\n+', text) if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    """Counts sentences based on sentence terminators. Edge case: empty string returns 1."""
    if not text.strip():
        return 1

    sentences = [s.strip() for s in re.findall(r'[^.!?]+(?:[.!?]|$)', text) if s.strip()]
    return len(sentences)

def run_analysis(text):
    print("--- Python Assessment: Text Analysis Results ---")
    
    # Word Count for 'Apple'
    apple_count = count_specific_word(text, "Apple")
    print(f"Specific word 'Apple' count: {apple_count}")
    
    # Most Common Word
    common = identify_most_common_word(text)
    print(f"Most common word: {common}")
    
    # Average Word Length
    avg_len = calculate_average_word_length(text)
    print(f"Average word length: {avg_len:.2f}")
    
    # Paragraph Count
    paragraphs = count_paragraphs(text)
    print(f"Paragraph count: {paragraphs}")
    
    # Sentence Count
    sentences = count_sentences(text)
    print(f"Sentence count: {sentences}")
    
    # Use of IF/ELSE as per criteria
    if apple_count > 10:
        print("This article mentions 'Apple' frequently.")
    else:
        print("This article has a low frequency of the word 'Apple'.")

if __name__ == "__main__":
    # Run the main analysis
    run_analysis(news_article)
    
    # Testing Edge Cases as requested
    print("\n--- Edge Case Testing ---")
    print(f"Empty String Paragraphs (Expected 1): {count_paragraphs('')}")
    print(f"Empty String Sentences (Expected 1): {count_sentences('')}")
    print(f"Empty String Word Length (Expected 0.0): {calculate_average_word_length('')}")
    print(f"Empty String Common Word (Expected None): {identify_most_common_word('')}")
