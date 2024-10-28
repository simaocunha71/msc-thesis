import re
def find_literals(string, pattern):
    """
    Search a string for a regex pattern and return the matching substring, a start index, and an end index.

    Parameters:
        string (str): The input string to search within.
        pattern (str): The regex pattern to search for.

    Returns:
        tuple: A tuple containing the matching substring, a start index, and an end index.

    """
    match = re.search(pattern, string)
    if match:
        return (match.group(0), match.start(), match.end())
    else:
        return None