import re


def split_sentences(paragraph):
    """
    Separates a paragraph into individual sentences,
    including sentences that begin with numbers.

    Parameters:
    paragraph (str): The paragraph entered by the user.

    Variables:
    sentences (list): Stores the individual sentences.
    sentence (str): Each sentence from the paragraph.

    Logic:
    1. Receive the paragraph entered by the user.
    2. Use regular expressions to split the paragraph
       at sentence-ending punctuation.
    3. Remove unnecessary whitespace.
    4. Store each sentence in a list.
    5. Return the list of sentences.

    Return:
    list: A list containing the individual sentences.
    """
    sentences = re.split(r'(?<=[.!?])\s+', paragraph.strip())
    sentences = [sentence.strip() for sentence in sentences
                 if sentence.strip()]
    return sentences


def main():
    """
    Gets a paragraph from the user and displays each
    individual sentence and the total sentence count.

    Parameters:
    None

    Variables:
    paragraph (str): The paragraph entered by the user.
    sentences (list): Stores the separated sentences.
    count (int): Stores the total number of sentences.
    sentence (str): Each sentence displayed to the user.

    Logic:
    1. Ask the user to enter a paragraph.
    2. Call the split_sentences function.
    3. Store the returned sentences in a list.
    4. Count the total number of sentences.
    5. Display each individual sentence.
    6. Display the total sentence count.

    Return:
    None
    """
    paragraph = input("Enter a paragraph: ")

    sentences = split_sentences(paragraph)
    count = len(sentences)

    print("\nIndividual Sentences:")
    for sentence in sentences:
        print(sentence)

    print("\nTotal number of sentences:", count)


if __name__ == "__main__":
    main()
