def remove_Occ(string,char):
    char_count = 0
    for i in range(len(string)):
        if(string[i] == char):
            char_count += 1
    if(char_count > 1):
        string = string[0:i+1] + string[i+1:-1*char_count] + string[len(string)-char_count:]
    return string