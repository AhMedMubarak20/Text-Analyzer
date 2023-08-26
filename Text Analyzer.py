def analyze_text(text):
    num_characters = len(text)
    num_words = len(text.split())
    num_lines = text.count('\n')

    print("Text analysis:")
    print(f"Number of characters: {num_characters}")
    print(f"Number of words: {num_words}")
    print(f"Number of lines: {num_lines}")

text = """This is a sample text for analyzing.
We will count characters, words, and lines.
Let's see how this works."""

analyze_text(text)
