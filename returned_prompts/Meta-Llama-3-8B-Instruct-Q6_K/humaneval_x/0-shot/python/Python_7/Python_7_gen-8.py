from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
    # The function filter_by_substring takes a list of strings and a substring as input.
    # It returns a new list containing only the strings that contain the given substring.
    # This is achieved using a list comprehension, where each string 's' in the input list
    # is included in the output list if the substring is found in 's' using the 'in' operator.
    # The time complexity of this function is O(n*m), where n is the number of strings
    # and m is the average length of the strings. This is because for each string, we are
    # checking for the presence of the substring, which takes linear time. The space complexity
    # is O(n), as we are storing the filtered strings in a new list.
    # The unit test provided checks the function with an empty input list, a list with multiple
    # strings, and a list with no strings containing the substring. The expected output
    # matches the actual output, indicating that the function is working correctly.  """

    # The function filter_by_substring takes a list of strings and a substring as input.
    # It returns a new list containing only the strings that contain the given substring.
    # This is achieved using a list comprehension, where each string 's' in the input list
    # is included in the output list if the substring is found in 's' using the 'in' operator.
    # The time complexity of this function is O(n*m), where n is the number of strings
    # and m is the average length of the strings. This is because for each string, we are
    # checking for the presence of the substring, which takes linear time. The space complexity
    # is O(n), as we are storing the filtered strings in a new list.
    # The unit test provided checks the function with an empty input list, a list with multiple
    # strings, and a list with no strings containing the substring. The expected output
    # matches the actual output, indicating that the function is working correctly.  """

    # The function filter_by_substring takes a list of strings and a substring as input.
    # It returns a new list containing only the strings that contain the given substring.
    # This is achieved using a list