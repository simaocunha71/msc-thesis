    if len(file_name) > 3:
        return "No"

    if file_name.count(".") != 1:
        return "No"

    if len(file_name.split(".")[0]) == 0:
        return "No"

    if file_name.split(".")[0][0].isalpha() == False:
        return "No"

    if file_name.split(".")[1] != "txt" and file_name.split(".")[1] != "exe" and file_name.split(".")[1] != "dll":
        return "No"

    return "Yes"


