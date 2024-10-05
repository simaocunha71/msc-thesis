
    def histogram(test):
        letter_dict = {}
        for letter in test.split():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

        max_value = max(letter_dict.values()) if letter_dict else 0

        return {k: v for k, v in letter_dict.items() if v == max_value}

    print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
    print(histogram('a b b a'))  # {'a': 2, 'b': 2}
    print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
    print(histogram('b b b b a'))  # {'b': 4}
    print(histogram(''))  # {}


The solution is to create a dictionary where the keys are the letters and the values are the number of times each letter appears in the string. We then find the maximum value in the dictionary, and return a new dictionary containing only the keys and values that have this maximum value.

The max function is used to find the maximum value in the dictionary. If the dictionary is empty, max will return 0.

The dictionary comprehension is used to create a new dictionary that only includes the keys and values where the value is equal to the maximum value.

In the end, we return the new dictionary.

This solution has a time complexity of O(n), where n is the number of letters in the string, because we are iterating over the string once. The space complexity is also O(n), because in the worst case, each letter in the string will be a key in the dictionary.

This solution assumes that the input string only contains lowercase letters and spaces. If the input string can contain uppercase letters or other characters, the solution will not work correctly.

"""

# Task 2
"""
