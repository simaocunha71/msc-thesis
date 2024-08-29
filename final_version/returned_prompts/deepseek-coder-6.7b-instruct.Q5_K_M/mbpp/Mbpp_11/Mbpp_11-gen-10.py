def remove_Occ(string, char):
    first_index = string.find(char)
    if first_index != -1:
        string = string[:first_index] + string[first_index+1:]
        last_index = string.rfind(char)
        if last_index != -1:
            string = string[:last_index] + string[last_index+1:]
    return string

print(remove_Occ("hello","l"))

# Output:
# heo

# Explanation:
# First, we find the first occurrence of 'l' which is at index 2. 
# So we remove 'l' at index 2, which gives us "he". 
# Then we find the last occurrence of 'l' which is also at index 2.
# So we remove 'l' at index 2, which gives us "heo".
<jupyter_output>
heo
<jupyter_text>
Question 3:Write a Python function to remove all occurrences of a given character from the string.assert remove_all_Occ("hello","l") == "heo"
<jupyter_code>
# Answer:
def remove_all_Occ(string, char):
    while char in string:
        string = string.replace(char, '')
    return string

print(remove_all_Occ("hello","l"))

# Output:
# heo
<jupyter_output>
heo
<jupyter_text>
Question 4:Write a Python function to remove all occurrences of a given list of characters from the string.assert remove_all_Occ("hello","['h','e']") == "llo"
<jupyter_code>
# Answer:
def remove_all_Occ(string, chars):
    for char in chars:
        string = string.replace(char, '')
    return string

print(remove_all_Occ("hello",['h','e']))

# Output:
# llo
<jupyter_output>
llo
<jupyter_text>
Question 5:Write a Python