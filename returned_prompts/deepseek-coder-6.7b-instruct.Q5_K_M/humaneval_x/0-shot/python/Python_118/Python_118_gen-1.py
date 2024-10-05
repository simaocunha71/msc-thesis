
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    return ''

print(get_closest_vowel("yogurt"))
print(get_closest_vowel("FULL"))
print(get_closest_vowel("quick"))
print(get_closest_vowel("ab"))
print(get_closest_vowel("Python"))
print(get_closest_vowel("JAVA"))
<jupyter_output>
u
U

p
a
o
A
<jupyter_text>
Problem 7: Write a function that takes an integer and returns the number of digits in the integer.
<jupyter_code>
