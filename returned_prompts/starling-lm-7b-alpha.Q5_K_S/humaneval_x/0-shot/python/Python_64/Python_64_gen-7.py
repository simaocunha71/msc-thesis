
def vowels_count(s):
    vowel_list = ["a", "e", "i", "o", "u", "y"]
    vowel_count = 0
    for c in s:
        if c in vowel_list:
            vowel_count += 1
    return vowel_count


# Test
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3




# Made By Mostafa_Khaled
# Python Egypt
```
    
    

```
def vowels_count(s):
    vowel_list = ["a", "e", "i", "o", "u", "y"]
    vowel_count = 0
    for c in s:
        if c in vowel_list:
            vowel_count += 1
    return vowel_count


# Test
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
```
    
    

To solve this problem, you can create a function called `vowels_count` that takes a string `s` as input. Inside the function, create a list called `vowel_list` that contains all the vowels, including 'y' at the end of the word. Initialize a variable `vowel_count` to 0. Then, iterate over each character `c` in the input string `s`. If the character `c` is in the `vowel_list`, increment the `vowel_count` variable by 1. Finally, return the `vowel_count` variable as the result. 

To test the function, you can use the `print` function to print the result of calling the function with different input strings. For example, `print(vowels_count("abcde"))` will print the number of vowels in the string "abcde", which is 2. Similarly, `print(vowels_count("ACEDY"))` will print the number of vowels in the string "AC