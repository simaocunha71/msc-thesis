
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    
    alphabet = "abcdefghijkmnpqrstuvxy"#
    encrypted_alphabet = ""   # create a new, empty list 
    for x in range(0, len(s),2):  # iterate over every two characters
        # get the last character of each pair that has an odd index  
        if (x % 2) == 1:     # check odd and even 
            encrypted_alphabet.append(alphabet[x%2])    # append it to list
    
    return ''.join(encrypted_alphabet)
            
# pass a string as an argument to encrypt  
def main():
    print('Enter a string: ')
    s = input()
    encrypted_s = encrypt(s) 
                       
    print("The alphabet is rotated down by two places.")    
print("Press 'q' to quit and 'r' to rotate the alphabet!")   # display the prompt for the user
                               
           