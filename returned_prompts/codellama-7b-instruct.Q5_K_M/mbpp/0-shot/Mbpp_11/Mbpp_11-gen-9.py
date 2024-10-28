def remove_Occ(str,char):
    if str.count(char)==0:
        return str
    first_index=str.find(char)
    last_index=str.rfind(char)
    return str[:first_index]+str[last_index+1:]
