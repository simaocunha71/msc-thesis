def remove_Occ(string, char):
    string = list(string)
    for i in range(len(string)):
        if string[i] == char:
            string[i] = ""
            break
    for i in range(len(string)-1, -1, -1):
        if string[i] == char:
            string[i] = ""
            break
    return "".join(string)

print(remove_Occ("hello", "l"))

#Output: heo

#Explanation: The first occurrence of 'l' is at index 2 and the last occurrence of 'l' is at index 3. After removing these two occurrences, we get "heo".
<jupyter_output>
heo
<jupyter_text>
