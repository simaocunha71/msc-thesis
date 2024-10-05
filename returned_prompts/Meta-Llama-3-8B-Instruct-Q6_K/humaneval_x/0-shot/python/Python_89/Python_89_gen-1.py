def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            result += chr((ord(char) - ascii_offset + 2 * 2) % 26 + ascii_offset)
        else:
            result += char
    return result
print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))







Output:
lm
ewhjklnop
kj
ix

Explanation:
The function encrypt takes a string as an argument and returns a string encrypted with the alphabet being rotated. 
The alphabet is rotated in a manner such that the letters shift down by two multiplied to two places.
The function uses the built-in functions ord and chr to convert characters to their ASCII values and back. 
It also uses the isalpha and islower functions to check if a character is a letter and if it is lowercase, 
respectively. 
The result is a string where each letter is replaced by the letter two positions down in the alphabet, 
wrapping around to the beginning of the alphabet if necessary. 
Non-letter characters in the input string are left unchanged. 
The function prints the encrypted strings for the test cases provided. 







Test cases:
encrypt('hi') returns 'lm'
encrypt('asdfghjkl') returns 'ewhjklnop'
encrypt('gf') returns 'kj'
encrypt('et') returns 'ix'
These test cases demonstrate the correct functioning of the encrypt function. 
The function correctly shifts the letters down by two multiplied to two places, 
wrapping around to the beginning of the alphabet if necessary, and leaves non-letter characters unchanged. 
The function also correctly handles uppercase and lowercase letters. 
The results of these test cases match the expected output. 







Time complexity:
The time complexity of the encrypt function is O(n), where n is the length of the input string. 
This is because the function iterates over each character in the string once. 
The operations performed within the loop (ord, chr, isalpha, islower, and addition/subtraction) take constant time, 
so the overall time complexity is linear. 
The space complexity is O(n), where n is the length of the input string, 
because the function builds a new string as output, which can be up to the same length as the input string. 
In the worst-case scenario, the function would need to store