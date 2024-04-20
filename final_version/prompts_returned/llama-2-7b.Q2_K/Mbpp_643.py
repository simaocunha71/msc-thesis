"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""

def text_match_wordz_middle(text):
    if not text:
        return 0
    else:
        found = False
        char_array = []
        
        for i in range(len(text)):
            if (i == 0 and text[i] != 'z'): break #found a match of 'z' at the start of the string
            elif (text[i:1] == "z"): break #found a 'z', now check for middle position
            else: char_array.append(text[i]) #add all characters to a list
            
        if text[0] != "z": found = True  #found a match of 'z' at the start of the string
        
        return found, char_array
    
if __name__=='__main__': pass