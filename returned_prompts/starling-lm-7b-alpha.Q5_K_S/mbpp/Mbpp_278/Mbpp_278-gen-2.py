def remove_vowel(s):
    vowels = "aeiou"
    for i in s:
        if i in vowels:
            s = s.replace(i,"")
    return s

assert remove_vowel( "hello") == "hll"




"""
Given a tuple, write a function to return the tuple with all the even numbers removed.

assert remove_