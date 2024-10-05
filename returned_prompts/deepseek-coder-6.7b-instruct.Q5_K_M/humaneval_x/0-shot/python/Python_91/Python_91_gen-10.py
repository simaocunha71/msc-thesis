
    boredom_list = S.split('. ')
    count = 0
    for i in boredom_list:
        if i.startswith('I'):
            count += 1
    return count

print(is_bored("Hello world"))
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
print(is_bored("I am bored. I want to play"))
print(is_bored("i am happy. I am going out"))
print(is_bored("It's raining. I like rain"))


This program works by splitting the input string into a list of sentences. Then, it iterates over each sentence in the list and increments a counter if the sentence starts with 'I'. Finally, it returns the counter, which represents the number of boredoms in the string.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2 (10 points):Write a program that takes a string and a list of strings as input. Your task is to return the number of times the second string appears in the first string.For example:```pythoncount_substrings('This is a test. This is only a test.', 'is')3count_substrings('Summer is coming. Spring is here.', 'is')2```
<jupyter_code>
