from collections import Counter
from string import punctuation

def load_text_file(path="", mode="r"):
    """
    Load the contents of a text file into a string.

    Parameters:
    path (str): The file path of the text file to be read. Defaults to an empty string.
    mode (str): The mode in which to open the file. Defaults to 'r' (read mode). 
                Other modes can be used as needed, such as 'r', 'w', 'a', 'wb', 'rb', 'ab' etc.

    Returns:
    str: The contents of the file as a string.

    Raises:
    FileNotFoundError: If the file specified by the `path` does not exist.
    IOError: If there is an issue opening or reading the file.
    """
    try:
        with open(path, mode) as f_in:
            file_text = f_in.read()
        return file_text
    
    except FileNotFoundError as e:
        # Handle the case where the file does not exist.
        print(f"Error: The file '{path}' does not exist.")
        raise e  # Re-raise the exception to signal that the file was not found.
    
    except IOError as e:
        # Handle other I/O related errors (e.g., permission issues).
        print(f"Error: An I/O error occurred while accessing the file '{path}'.")
        raise e  # Re-raise the exception to signal that an I/O error occurred.

def clean_text(text=""):
    """
    Clean a given text by converting it to lowercase and removing punctuation.

    Parameters:
    text (str): The text to be cleaned. Defaults to an empty string.

    Returns:
    str: The cleaned text with all characters in lowercase and punctuation removed.

    Example:
    >>> clean_text("Hello, World!")
    'hello world'
    
    Notes:
    - This function uses `string.punctuation` to identify punctuation characters.
    - The input `text` should be a string. If it is not a string, an AssertionError will be raised.
    """
    # Assert that the input is a string
    assert isinstance(text, str), "Input must be a string"

    # Convert text to lowercase
    text = text.lower()
    
    # Remove each punctuation character
    for p in punctuation:
        text = text.replace(p, '')
    
    return text

def count_words(path):
    """
    Count the occurrences of each word in a text file.

    Parameters:
    path (str): The file path of the text file to be read.

    Returns:
    collections.Counter: A Counter object where keys are words and values are the counts of those words.

    Raises:
    FileNotFoundError: If the file specified by the `path` does not exist.
    IOError: If there is an issue opening or reading the file.
    TypeError: If the `path` is not a string.

    Example:
    >>> count_words("example.txt")
    Counter({'word1': 5, 'word2': 3, ...})

    Notes:
    - This function uses `load_text_file` to read the file and `clean_text` to preprocess the text.
    - Ensure that `load_text_file` and `clean_text` are correctly implemented and available in the scope.
    """
    
    # Check if the path is a string and raise a TypeError if it is not
    if not isinstance(path, str):
        raise TypeError("The path must be a string")

    # Load and clean the text from the file
    text_file = load_text_file(path, mode="r")
    text_file_cleaned = clean_text(text_file)
    
    # Split the cleaned text into words and count their occurrences
    words = text_file_cleaned.split()
    return Counter(words)