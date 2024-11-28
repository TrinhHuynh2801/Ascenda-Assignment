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

def lower_and_trim(string: str) -> str:
    """
    Lowercase the first letter of the string and every letter after a space, trimming extra spaces.
    
    Args:
        string (str): The input string (e.g., 'JOHN DOE').
        
    Returns:
        str: The string with each word in lowercase (e.g., 'john doe').
    """
    return ' '.join(word.lower() for word in string.split())

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

def remove_special_and_lower(string: str) -> str:
    """
    Remove special characters from the string, keep spaces between words, and convert it to lowercase.
    
    Args:
        string (str): The input string with special characters and spaces (e.g., 'Hello@ World!').
        
    Returns:
        str: The string with special characters removed, spaces retained, and in lowercase (e.g., 'hello world').
    """
    # Remove all non-alphanumeric characters except spaces
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', trim(string))
    
    # Convert the string to lowercase
    return cleaned_string.lower()

def clean_string(string: str) -> str:
    """
    Remove special characters and spaces, and convert the string to lowercase.
    
    Args:
        string (str): The input string (e.g., 'Hello@ World!').
        
    Returns:
        str: A cleaned string with no spaces or special characters, in lowercase.
    """
    # Remove all non-alphanumeric characters except spaces
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string)
    
    # Convert to lowercase
    cleaned_string = cleaned_string.lower()
    
    return cleaned_string