
    def split_words(txt):
        words = txt.split(' ')
        if len(words) == 1:
            words = txt.split(',')
            if len(words) == 1:
                return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0)
        return words

    print(split_words("Hello world!"))  # ➞  ["Hello", "world!"]
    print(split_words("Hello,world!"))  # ➞  ["Hello", "world!"]
    print(split_words("abcdef"))  # ➞ 3


'''
Explanation:
In the function split_words, first, we check if the string txt is split by whitespace. If it is not split by whitespace we split by comma. If the string is still not split by whitespace or comma, we count the number of lower case letters with odd index in the alphabet.
'''

'''
The function split_words is defined by taking a string txt as an argument. The function checks the string if it is split by whitespace and if it is not, it splits the string by commas. If the string is still not split, it counts the number of lower case letters with odd index in the alphabet and returns the count.
'''

'''
The function split_words("Hello world") returns ["Hello", "world"], since the string is split by whitespace.
The function split_words("Hello,world") returns ["Hello", "world"], since the string is split by comma.
The function split_words("abcdef") returns 3, since there are 3 lower case letters with odd index in the alphabet.
'''

'''
The function split_words("Hello world") returns ["Hello", "world"], since the string is split by whitespace.
The function split_words("Hello,world") returns ["Hello", "world"], since the string is split by comma.
The function split_words("abcdef") returns 3, since there are 3 lower case letters with odd index in the alphabet.
'''

'''
The function split_words("Hello world") returns ["Hello",