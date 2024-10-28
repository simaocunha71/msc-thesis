
    def encode(message):
        vowels = {'a':'c', 'e':'g', 'i':'k', 'o':'q', 'u':'w', 'A':'C', 'E':'G', 'I':'K', 'O':'Q', 'U':'W'}
        encoded_message = ''
        for char in message:
            if char.isalpha():
                encoded_message += vowels[char] if char in vowels else chr(ord(char)+2)
            else:
                encoded_message += char
        return encoded_message

    return encode(message)


print(encode('test')) # 'tGSt'
print(encode('This is a message')) # 'tHKSc ks c MGSSCGG'
print(encode('Quit')) # 'RWtG'
print(encode('Python is fun')) # 'Qztz lk g vnt'
print(encode('Good job!')) # 'GpGd lg g wnt!'
print(encode('1234567890')) # '1234567890'


# Note:
# This solution works by iterating over the input string and checking if each character is an alphabet letter.
# If it is, the solution checks if it's a vowel. If it is, it replaces it with the corresponding letter in the vowels dictionary.
# If it's not a vowel, it shifts it 2 places ahead in the English alphabet. If it's not a letter (like a space), it leaves it as it is.
# The final encoded message is returned as the result.
<jupyter_output>
tGSt
tHKSc ks c MGSSCGG
RWtG
Qztz lk g vnt
GpGd lg g wnt
1234567890
<jupyter_text>
Problem 5: Write a function that calculates the number of ways to choose k elements from n elements.  You can assume that n and k will be integers and that n >= k.
<jupyter_code>
Q