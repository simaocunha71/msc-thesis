def long_words(n,sentence):
    words=sentence.split()
    long_words=[]
    for i in words:
        if len(i)>n:
            long_words.append(i)
    return long_words

long_words(3,"python is a programming language")


"""
The function long_words should return a list of words that are longer than n in the sentence provided. The function long_words takes in two parameters, n and the sentence. The function first splits the sentence into a list of words. It then loops through the list of words, and if a word is longer than n characters, it adds that word to the long_words list. Finally, the function returns the long_words list.
"""

"""
To test the function long_words, you can use the provided assert statement. This statement asserts that when you call long_words with the arguments 3 and "python is a programming language", the function should return ['python','programming','language']. You can use the print statement to print the result of the function call to see if the assertion is true.
"""

# long_words(3,"python is a programming language")

"""
The output of the above code will be ['python', 'programming', 'language'] because these are the words in the sentence "python is a programming language" that are longer than 3 characters.
"""

# Here is a step-by-step explanation of the solution:

# 1. Define the function long_words that takes in two parameters, n and sentence.
# 2. Split the sentence into a list of words using the split() method and store the result in the variable words.
# 3. Create an empty list called long_words to store the words that are longer than n.
# 4. Use a for loop to iterate through each word in the words list.
# 5. Inside the loop, check if the length of the current word is greater than n using the len() function. If it is, add the word to the long_words list using the append() method.
# 6. After the loop, return the long_words list.
# 7. Use the provided assert statement to test the function long_words with the arguments 3 and "python is a programming language