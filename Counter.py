def count_words(text):

    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    if not text.strip():
        return 0
    words = text.split()
    return len(words)

# Main loop for user interaction
while True:
    user_input = input("Please enter a sentence or paragraph (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    word_count = count_words(user_input)
    print(f"The number of words in the input is: {word_count}")
