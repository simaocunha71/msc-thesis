
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split(' ')
    result = ''

    for word in words:
        if is_prime(len(word)):
            result += word + ' '

    return result.rstrip()

print(words_in_sentence("This is a test"))
print(words_in_sentence("lets go for swimming"))
print(words_in_sentence("Python code is cool"))
print(words_in_sentence("QA is about quality"))
<jupyter_output>
is
go for
Python code is
QA is about quality
<jupyter_text>
4. Write a Python function named `anagrams` that takes a list of strings and returns a list of all anagram groups from the input list. The order of the strings in the output list should be the same as the input list. The order of the strings within each anagram group should be the same as in the input list.
<jupyter_code>
