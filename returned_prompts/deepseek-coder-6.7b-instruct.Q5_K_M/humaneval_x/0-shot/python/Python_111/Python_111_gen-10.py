
    def histogram(test):
        test = test.split()
        test_dict = {}
        for letter in test:
            if letter in test_dict:
                test_dict[letter] += 1
            else:
                test_dict[letter] = 1
        max_value = max(test_dict.values())
        return {key: value for key, value in test_dict.items() if value == max_value}

    print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
    print(histogram('a b b a'))  # {'a': 2, 'b': 2}
    print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
    print(histogram('b b b b a'))  # {'b': 4}
    print(histogram(''))  # {}

"""
This solution uses a dictionary to count the occurrence of each letter. 
Then, it finds the maximum occurrence and returns a dictionary with the letters that have this occurrence.
"""

"""
The time complexity for this solution is O(n), where n is the number of words in the string. 
The space complexity is also O(n), as in the worst case scenario (when all words are unique), the size of the dictionary will be equal to the number of words.
"""

"""
This solution assumes that the input string consists only of lowercase letters and spaces. 
If there may be uppercase letters, numbers or special characters, the function needs to be adjusted accordingly.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:
<jupyter_code>
