
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            count += 1
    return count

# Test cases
print(count_upper('aBCdEf')) # should return 1
print(count_upper('abcdefg')) # should return 0
print(count_upper('dBBE')) # should return 0
print(count_upper('AaBe')) # should return 1
print(count_upper('bBbB')) # should return 0
print(count_upper('ABcDE')) # should return 1
print(count_upper('aABbCCdDEE')) # should return 2
<jupyter_output>
1
0
0
1
0
1
2
<jupyter_text>
Problem 2: Write a function to reverse each word in a sentence. For example, given the input string "Hello World", the function should return "olleH dlroW".
<jupyter_code>
def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())

# Test cases
print(reverse_words('Hello World')) # should return "olleH dlroW"
print(reverse_words('Python is fun')) # should return "nohtyP si nuf"
print(reverse_words('I love programming')) # should return "I evol gnimmargorp"
<jupyter_output>
olleH dlroW
nohtyP si nuf
I evol gnimmargorp
<jupyter_text>
Problem 3: Write a function that takes a string and returns a dictionary where the keys are the characters in the string and the values are their corresponding counts. For example, given the input string "hello", the function should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}.
<jupyter_code>
def count_chars(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 