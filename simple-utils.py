# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverse the characters in the given string.
    
    Parameters:
        text (str): Input string to reverse.
    
    Returns:
        str: The input string with its characters in reverse order.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count words in a string by splitting on whitespace.
    
    Parameters:
    	sentence (str): Input text; words are determined by splitting on whitespace characters.
    
    Returns:
    	int: Number of words produced by splitting `sentence` on whitespace.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius.
    
    Returns:
        float: Equivalent temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32