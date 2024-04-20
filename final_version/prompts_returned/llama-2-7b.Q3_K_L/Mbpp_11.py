"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""

def remove_Occ(s, c):
    if not isinstance(s, str) or not isinstance(c, str) :
        return (None , None )
        
    # check if the string is empty
    if s.strip() == "":
        return (None , None) 
    
    # Split the string into a list of characters
    chars = [s[i] for i,c in enumerate(s)]
    first_occurence= None
    last_occurence= None
    n=0
    while True:
        if n >= len(chars):
            break
        if chars[n]== c:
            if not first_occurence or (first_occurence < n):
                first_occurence = n
            else:
                
                
                #remove the first occurance of the character from list and change it's position to last element of the list. 
                chars[n-1], chars[0] = chars[0] , chars[1+first_occurence]
    
    return (chars[ : -first_occurence +1] , chars[-first_occurrence:])