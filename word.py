def word_count(text):
    words = text.split()
    return len(words)

data = "This is a test sentence with multiple words."
print(word_count(data))