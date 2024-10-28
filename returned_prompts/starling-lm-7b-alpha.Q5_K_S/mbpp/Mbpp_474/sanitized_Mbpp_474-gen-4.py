def replace_char(string,char_rep,char_rep_with):
    for i in range(len(string)):
        if string[i] == char_rep:
            string = string[:i] + char_rep_with + string[i+1:]
    return string