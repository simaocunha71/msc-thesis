    if value.find(".") == -1:
        return int(value)
    else:
        if value.split(".")[1] == "0":
            return int(value)
        elif value.split(".")[1][0] == "5":
            return int(value) + 1
        else:
            return int(value)
