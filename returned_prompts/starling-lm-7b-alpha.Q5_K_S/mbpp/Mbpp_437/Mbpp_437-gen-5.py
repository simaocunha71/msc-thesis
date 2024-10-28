
def remove_odd(string):
    string_list = list(string)
    for i in range(len(string_list)):
        if i%2==0:
            string_list[i]=string_list[i]
    return "".join(string_list)


