
    str_list = [str(x) for x in str(x)]
    if shift > len(str_list):
        return "".join(reversed(str_list))
    else:
        return "".join(str_list[shift:] + str_list[:shift])
