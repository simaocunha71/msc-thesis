    result = []
    for idx in range(1, n + 1):
        if idx % 2 == 0:
            result.append(fact(idx))
        else:
            result.append(sum_from_one_to(idx))
    return result


def fact(n):
    """ Implement the function fact that takes n as a parameter and returns the factorial of n
    Example:
    fact(5) == 120
    """

    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def sum_from_one_to(n):
    """ Implement the function sum_from_one_to that takes n as a parameter and returns the sum of numbers from 1 to n
    Example:
    sum_from_one_to(5) == 15
    """

    if n == 1:
        return 1
    else:
        return n + sum_from_one_to(n - 1)


def count_words(words):
    """
    Implement the function count_words that takes a string with multiple words and returns a dictionary with the number of
    occurrences of each word in the string. The keys of the dictionary should be the words, and the values should be the
    number of occurrences of the corresponding word in the string.
    Example:
    count_words("I am feeling good") == {'I': 1, 'am': 1, 'feeling': 1, 'good': 1}
    """

    result = {}
    for word in words.split():
        if word not in result:
            result[word] = 0
        result[word] += 1
    return result


def count_letters(words):
    """
    Implement the function count_letters that takes a string with multiple words and returns a dictionary with the number of
    occurrences of each letter in the string. The keys of the dictionary should be the letters (case insensitive), and the values
    should be the number of occurrences of the corresponding letter in the string.
    Example:
    count_letters("I am feeling good") ==