
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

    if len(sentence) < 2 or len(sentence) > 45:
        return ""
    words = sentence.split()[:] # the original string containing the words separated by a space
    result_string = ''
    for word in words:
        # convert the length of each character in word to an int
        char_lengths = [int(c) for c in word]
        prime_nums = [1, 3, 5] # three prime numbers
        for i in range(0, len(prime_nums)):
            if (not any([int(c) % int(prime_nums[i]) == 0 for c in char_lengths])): # check if the length of each character is a multiple of the current prime number
                break
        else: # if every character isn't a multiple of the current prime number, we add it to the result_string
            if any([int(c) % int(prime_nums[i]) != 0 for c in char_lengths]):
                result_string = word + " " + result_string
    return result_string # the new string formed of the original words, each having length a prime number. The order is preserved.
    """
    # Coding Challenge 14 Solution:
    # You are given a sentence and your task is to print only its words whose lengths are prime numbers on a single line with the length of each word following it separated by a space.
    # So basically