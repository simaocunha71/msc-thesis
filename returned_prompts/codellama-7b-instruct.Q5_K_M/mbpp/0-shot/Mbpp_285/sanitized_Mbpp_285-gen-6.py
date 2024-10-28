def text_match_two_three(string):
    if string.count("a") == 0:
        return False
    else:
        index_a = string.index("a")
        if string[index_a+1:index_a+3] == "bb" or string[index_a+1:index_a+4] == "bbb":
            return True
        else:
            return False