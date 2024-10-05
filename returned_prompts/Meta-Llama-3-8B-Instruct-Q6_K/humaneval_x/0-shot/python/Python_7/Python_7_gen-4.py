from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]  # use list comprehension
    # or, using a for loop
    # result = []
    # for s in strings:
    #     if substring in s:
    #         result.append(s)
    # return result
    # or, using filter function
    # return list(filter(lambda s: substring in s, strings))
    # or, using a generator expression
    # return list(g for g in (s for s in strings if substring in s))  # in Python 3.0+
    # in Python 2.x, use itertools.imap instead of generator expression
    # return list(itertools.imap(lambda s: substring in s, strings))
    # or, using a regular expression
    # import re
    # return [s for s in strings if re.search(substring, s)]
    # or, using a for loop with if statement
    # result = []
    # for s in strings:
    #     if substring in s:
    #         result.append(s)
    # return result
    # ...and so on
    # The choice of method is a matter of personal preference and the specific requirements of the problem.  # The list comprehension is generally the most concise and readable.  # If the input list is very large, a generator expression or filter function might be more memory-efficient.  # If the substring is very large, a regular expression might be more efficient.  # If the substring is a fixed string, a for loop with if statement might be more readable.  # And so on.  # The key is to choose the method that best fits the specific requirements of the problem.  # In general, it's a good idea to start with the most concise and readable method and then optimize as needed.  # In this case, the list comprehension is a good choice because it's concise and readable.  # It's also easy to understand and maintain, which is important for a function that's intended to be used by others.  # It's also easy to test and debug, which is important for a function that's intended to be used in a production environment.  # In summary, the list comprehension is a good choice because it's concise, readable, easy to understand and maintain, easy to test and debug, and efficient.  # It