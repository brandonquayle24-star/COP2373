import re


def validate_phone(phone):
    """
    Validates a phone number using regular expressions.

    Parameters:
    phone (str): The phone number entered by the user.

    Variables:
    pattern (str): Regular expression used to check the phone number.

    Logic:
    1. Define the required phone number format XXX-XXX-XXXX.
    2. Use re.fullmatch to compare the phone number to the pattern.
    3. Convert the match result into a Boolean value.
    4. Return True if the format matches, otherwise False.

    Return:
    bool: True if the phone number is valid, otherwise False.
    """
    pattern = r"\d{3}-\d{3}-\d{4}"
    return bool(re.fullmatch(pattern, phone))


def validate_ssn(ssn):
    """
    Validates a Social Security number using regular expressions.

    Parameters:
    ssn (str): The Social Security number entered by the user.

    Variables:
    pattern (str): Regular expression used to validate the SSN.

    Logic:
    1. Define the required SSN format XXX-XX-XXXX.
    2. Check that the first three digits are not 000, 666,
       or between 900 and 999.
    3. Check that the middle two digits are not 00.
    4. Check that the final four digits are not 0000.
    5. Use re.fullmatch to validate the SSN.
    6. Return True if the SSN passes all checks.

    Return:
    bool: True if the SSN passes validation, otherwise False.
    """
    pattern = r"(?!000|666|9\d{2})\d{3}-(?!00)\d{2}-(?!0000)\d{4}"
    return bool(re.fullmatch(pattern, ssn))


def validate_zip(zip_code):
    """
    Validates a ZIP code using regular expressions.

    Parameters:
    zip_code (str): The ZIP code entered by the user.

    Variables:
    pattern (str): Regular expression used to validate ZIP codes.

    Logic:
    1. Define the five-digit ZIP code format.
    2. Allow an optional hyphen followed by four additional digits.
    3. Use re.fullmatch to compare the ZIP code to the pattern.
    4. Return True if the ZIP code matches either format.

    Return:
    bool: True if the ZIP code is valid, otherwise False.
    """
    pattern = r"\d{5}(-\d{4})?"
    return bool(re.fullmatch(pattern, zip_code))


def main():
    """
    Collects user information and displays validation results.

    Parameters:
    None

    Variables:
    phone (str): Phone number entered by the user.
    ssn (str): Social Security number entered by the user.
    zip_code (str): ZIP code entered by the user.

    Logic:
    1. Display the program title.
    2. Ask the user to enter a phone number.
    3. Ask the user to enter a Social Security number.
    4. Ask the user to enter a ZIP code.
    5. Call validate_phone to check the phone number.
    6. Display whether the phone number is valid or invalid.
    7. Call validate_ssn to check the Social Security number.
    8. Display whether the SSN is valid or invalid.
    9. Call validate_zip to check the ZIP code.
    10. Display whether the ZIP code is valid or invalid.

    Return:
    None
    """
    print("Phone Number, SSN, and ZIP Code Validator")

    phone = input("Enter phone number (XXX-XXX-XXXX): ")
    ssn = input("Enter SSN (XXX-XX-XXXX): ")
    zip_code = input("Enter ZIP code: ")

    print("\nValidation Results:")

    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    if validate_ssn(ssn):
        print("Social Security number is valid.")
    else:
        print("Social Security number is invalid.")

    if validate_zip(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")


if __name__ == "__main__":
    main()
