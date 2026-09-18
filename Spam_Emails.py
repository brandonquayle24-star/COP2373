# Brandon Quayle
# Spam Email Detector
# This program checks an email message for common spam words and phrases.
# It calculates a spam score and displays the likelihood that the message is spam.


# Function to calculate the spam score and find spam words
def check_spam(email_message, spam_words):
    """
    Checks an email message for common spam words and phrases
    and calculates the spam score.

    Parameters:
        email_message (str): The email message entered by the user.
        spam_words (list): The list of common spam words and phrases.

    Variables:
        spam_score (int): Keeps track of the spam score.
        found_words (list): Stores spam words and phrases found.
        word (str): The current spam word or phrase being checked.
        count (int): Number of times the word or phrase appears.

    Logic:
        1. Set the spam score to zero.
        2. Create an empty list for found spam words.
        3. Convert the email message to lowercase.
        4. Loop through the spam word list.
        5. Count each occurrence of a spam word or phrase.
        6. Add each occurrence to the spam score.
        7. Store matching words or phrases in found_words.
        8. Return the spam score and found words.

    Return:
        spam_score (int): The final spam score.
        found_words (list): The spam words and phrases found.
    """

    spam_score = 0
    found_words = []

    email_message = email_message.lower()

    for word in spam_words:
        count = email_message.count(word.lower())

        if count > 0:
            spam_score += count
            found_words.append(word)

    return spam_score, found_words


# Function to determine the likelihood that the email is spam
def spam_likelihood(spam_score):
    """
    Determines how likely an email message is to be spam
    based on the spam score.

    Parameters:
        spam_score (int): The calculated spam score.

    Variables:
        None

    Logic:
        1. Check the value of the spam score.
        2. If the score is 0, return Very unlikely to be spam.
        3. If the score is 1 or 2, return Unlikely to be spam.
        4. If the score is 3 through 5, return Possibly spam.
        5. If the score is 6 through 9, return Likely to be spam.
        6. Otherwise, return Very likely to be spam.

    Return:
        str: The likelihood that the email message is spam.
    """

    if spam_score == 0:
        return "Very unlikely to be spam"
    elif spam_score <= 2:
        return "Unlikely to be spam"
    elif spam_score <= 5:
        return "Possibly spam"
    elif spam_score <= 9:
        return "Likely to be spam"
    else:
        return "Very likely to be spam"


# Main function
def main():
    """
    Runs the Spam Email Detector program and displays the results.

    Parameters:
        None

    Variables:
        spam_words (list): Contains the 30 common spam words and phrases.
        email_message (str): The email message entered by the user.
        spam_score (int): The calculated spam score.
        found_words (list): Stores spam words and phrases found.
        likelihood (str): The likelihood that the message is spam.

    Logic:
        1. Create a list of 30 common spam words and phrases.
        2. Display the program heading.
        3. Ask the user to enter an email message.
        4. Call check_spam to calculate the spam score.
        5. Call spam_likelihood to determine the likelihood of spam.
        6. Display the spam score and likelihood.
        7. Display the spam words and phrases that were found.

    Return:
        None
    """

    spam_words = [
        "free",
        "winner",
        "congratulations",
        "click here",
        "act now",
        "limited time",
        "urgent",
        "cash",
        "prize",
        "guaranteed",
        "risk free",
        "special offer",
        "buy now",
        "order now",
        "credit",
        "loan",
        "earn money",
        "make money",
        "extra income",
        "work from home",
        "no cost",
        "100% free",
        "claim now",
        "you have won",
        "selected",
        "exclusive deal",
        "lowest price",
        "save big",
        "bonus",
        "unsubscribe"
    ]

    print("Spam Email Detector")
    print("-------------------")

    email_message = input("Enter the email message you want to check:\n")

    spam_score, found_words = check_spam(email_message, spam_words)

    likelihood = spam_likelihood(spam_score)

    print("\nSpam Analysis")
    print("-------------")
    print("Spam Score:", spam_score)
    print("Likelihood:", likelihood)

    if found_words:
        print("\nSpam words/phrases found:")

        for word in found_words:
            print("-", word)
    else:
        print("\nNo spam words or phrases were found.")


if __name__ == "__main__":
    main()


