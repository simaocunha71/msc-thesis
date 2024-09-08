def remove_Occ(string, char):
    first_index = string.find(char)
    if first_index != -1:
        string = string[:first_index] + string[first_index+1:]
        last_index = string.rfind(char)
        if last_index != -1:
            string = string[:last_index] + string[last_index+1:]
    return string