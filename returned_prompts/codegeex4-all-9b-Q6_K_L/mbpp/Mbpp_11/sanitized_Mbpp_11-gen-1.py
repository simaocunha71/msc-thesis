def remove_Occ(string, char):
    # Find the index of the first occurrence of char
    first_occ = string.find(char)
    
    # Find the index of the last occurrence of char
    last_occ = string.rfind(char)
    
    # Remove the first occurrence of char
    if first_occ != -1:
        string = string[:first_occ] + string[first_occ + 1:]
    
    # Remove the last occurrence of char
    if last_occ != -1:
        string = string[:last_occ] + string[last_occ + 1:]
    
    return string