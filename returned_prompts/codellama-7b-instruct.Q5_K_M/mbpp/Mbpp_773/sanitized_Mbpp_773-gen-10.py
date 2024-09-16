def occurance_substring(main_string,substring):
    pos=main_string.find(substring)
    if pos==-1:
        return None
    else:
        return (substring,pos,pos+len(substring))