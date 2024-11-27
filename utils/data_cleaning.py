# utils/data_clean.py
import re

def upper_and_trim(string: str) -> str:
    """
    Uppercase the first letter of the string and every letter after a space.
    
    Args:
        name (str): The input string (e.g., 'john doe').
        
    Returns:
        str: The string with each word capitalized (e.g., 'John Doe').
    """
    return ' '.join(word.capitalize() for word in string.split())

def trim(string: str) -> str:
    """
    Trim leading and trailing spaces from the string without changing case.
    """
    return string.strip()

def remove_special_chars(string: str) -> str:
    """
    Remove any characters from the text that are not alphanumeric or in the allowed set of characters.
    Preserves letters, numbers, spaces, and a set of punctuation marks.
    
    Args:
        text (str): The input string to be cleaned.
        
    Returns:
        str: The cleaned string with only the allowed characters.
    """
    return re.sub(r'[^a-zA-Z0-9\s.,!?;:()\'"-/]', '', trim(string))