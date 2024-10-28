

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))


print(count_distinct_characters('xyzXYZ'))
print(count_distinct_characters('Jerry'))


'''
Explanation: 

In the function, we first convert the given string to lowercase using the string.lower() function. 
Then we convert it to a set using the set() function. In Python, a set is a collection which is unordered and unindexed. 
The set function removes all duplicate characters in the string. Finally, we return the length of the set using the len() function. 
This length is the number of distinct characters in the string.
'''

'''
Alternative solution:

def count_distinct_characters(string: str) -> int:
    count = 0
    checked = []

    for char in string.lower():
        if char not in checked:
            count += 1
            checked.append(char)

    return count


print(count_distinct_characters('xyzXYZ'))
print(count_distinct_characters('Jerry'))
'''

'''
Explanation: 

In this solution, we first convert the given string to lowercase. We then initialize a count variable to 0 and an empty list checked. 
We iterate over each character in the string. If the character is not in the checked list, we increment the count and add the character to the checked list. 
Finally, we return the count which is the number of distinct characters.
'''
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: String Rotation
<jupyter_code>
