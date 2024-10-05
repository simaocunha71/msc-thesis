    if len(file_name.split(".")[0]) > 3:
        return "No"
    elif file_name.count(".") != 1:
        return "No"
    elif file_name[0] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "No"
    elif file_name.split(".")[1] not in ["exe", "dll", "txt"]:
        return "No"
    else:
        return "Yes"

