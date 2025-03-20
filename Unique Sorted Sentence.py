def sentence(sentence_str: str) -> str:
    words = sentence_str.split()  # Split the sentence into words
    unique_words = []  # List to store non-repeating words

    for word in words:  # Iterate through the list
        if word not in unique_words:  # If the word hasn't been added before
            unique_words.append(word)  # Add it to the list

    unique_words.sort()  # Sort the list alphabetically
    return ' '.join(unique_words)  # Join the words and return as a string

sentence_str = input("Enter a sentence: ")
print(sentence(sentence_str))
