def remove_Occ(s, c):
    first = s.find(c)
    if first != -1:
        last = s.rfind(c)
        return s[:first] + s[first+1:last] + s[last+1:]
    else:
        return s

print(remove_Occ("hello","l"))

#output: heo

#Explanation: 
#First occurrence of 'l' is at index 2 and last occurrence of 'l' is at index 3. So, we remove these 'l's from the string.

#The function find() is used to get the first occurrence of the character and rfind() is used to get the last occurrence of the character.
#Then, we use slicing to get the string after removing the first and last occurrence of the character.
#If the character does not exist in the string, the function will return the string as it is.

#This code works for all strings and all characters. It will return the string after removing the first and last occurrence of the character.

#The time complexity of this code is O(n), where n is the length of the string. This is because it needs to traverse the string to find the first and last occurrence of the character.
#The space complexity is O(n), as we are creating a new string which is the modified version of the original string.

#I hope this helps you understand the problem and the solution. Let me know if you have any other questions.
<jupyter_output>
<empty_output>
<jupyter_text>
