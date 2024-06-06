import string
import getpass


def check_password_strength(password):
    """Analyzes the strength of a password.

    Args:
        password (str): The password to be checked.

    Returns:
        int: The calculated password strength score (out of 5).
    """

    strength = 0
    remarks = ''
    char_counts = {
        'lowercase': 0,
        'uppercase': 0,
        'digits': 0,
        'whitespace': 0,
        'special': 0,
    }

    # Minimum length check
    if len(password) < 8:
        strength = 0
        remarks = 'Password is too short. Minimum length is 8 characters.'
        return strength, remarks

    # Character analysis
    for char in password:
        if char in string.ascii_lowercase:
            char_counts['lowercase'] += 1
        elif char in string.ascii_uppercase:
            char_counts['uppercase'] += 1
        elif char in string.digits:
            char_counts['digits'] += 1
        elif char == ' ':
            char_counts['whitespace'] += 1
        else:
            char_counts['special'] += 1

    # Strength scoring based on character class distribution
    strength += 1 if char_counts['lowercase'] >= 1 else 0
    strength += 1 if char_counts['uppercase'] >= 1 else 0
    strength += 1 if char_counts['digits'] >= 1 else 0
    strength += 1 if char_counts['whitespace'] == 0 else -1  # Penalize whitespaces
    strength += 1 if char_counts['special'] >= 1 else 0

    if strength == 1:
        remarks = 'Very weak password. Use more character types!'
    elif strength == 2:
        remarks = 'Weak password. Consider adding more complexity.'
    elif strength == 3:
        remarks = 'Okay password, but it can be stronger.'
    elif strength == 4:
        remarks = 'Strong password. Keep it secret!'
    elif strength == 5:
        remarks = 'Excellent password! Hackers stand no chance.'

    return strength, remarks


def check_pwd(another_pw=False):
    """Prompts the user to check another password.

    Args:
        another_pw (bool, optional): Whether to check another password. Defaults to False.

    Returns:
        bool: True if the user wants to check another password, False otherwise.
    """

    valid = False
    if another_pw:
        choice = input(
            'Do you want to check another password\'s strength (y/n) : ')
    else:
        choice = input(
            'Do you want to check your password\'s strength (y/n) : ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print('Exiting...')
            return False
        else:
            print('Invalid input...please try again. \n')
