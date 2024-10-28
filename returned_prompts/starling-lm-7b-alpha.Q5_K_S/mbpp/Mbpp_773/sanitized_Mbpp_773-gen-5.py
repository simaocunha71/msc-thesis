def occurance_substring(str,substr):
    # your code here
    if substr not in str:
        return None
    else:
        return (substr, str.index(substr), str.index(substr)+len(substr))