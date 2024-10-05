
    def words_in_sentence(sentence):
        # function to check if a number is prime
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

        words = sentence.split()
        result = []
        for word in words:
            if is_prime(len(word)):
                result.append(word)
        return " ".join(result)

    print(words_in_sentence("This is a test"))
    print(words_in_sentence("lets go for swimming"))

This code first defines a helper function `is_prime()` to check if a given number is a prime number. Then, it splits the input sentence into words and checks the length of each word. If the length is a prime number, it appends the word to the `result` list. Finally, it joins the words in the `result` list with spaces and returns the result.

The helper function `is_prime()` checks each number from 2 to `n` to see if `n` is divisible by it. If `n` is divisible by any number in this range, it is not a prime number and the function returns `False`. If `n` is not divisible by any number in this range, it is a prime number and the function returns `True`. Note that this function checks if the number is prime for all integers greater than 1.

The main function `words_in_sentence()` splits the input sentence into words, checks the length of each word, and appends the word to the `result` list if the length is a prime number. It then joins the words in the `result` list with spaces and returns the result.

The time complexity of this code is O(n*m), where n is the number of words in the sentence and m is the average length of the words. This is because for each word, the code checks if its length is a prime number by iterating from 2 to the length of the word. The space complexity is O(n), where n is the number of words in the sentence, because the code stores the words in a list.
