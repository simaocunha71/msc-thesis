
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split(' ')
    res = []
    for word in words:
        if is_prime(len(word)):
            res.append(word)
    return ' '.join(res)


print(words_in_sentence("This is a test"))  # "is"
print(words_in_sentence("lets go for swimming"))  # "go for"

#Time Complexity: O(n*sqrt(m)), where n is the number of words in the sentence and m is the length of the longest word.
#Space Complexity: O(n), where n is the number of words in the sentence.
<jupyter_output>
is
go for
<jupyter_text>
Problem 3
<jupyter_code>
