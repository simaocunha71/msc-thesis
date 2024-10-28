    if file_name.isalnum():
        if len(file_name) > 3:
            return "No"
        else:
            if file_name.count(".") == 1:
                if file_name.split(".")[0] == "":
                    return "No"
                else:
                    if file_name.split(".")[1] in ["txt", "exe", "dll"]:
                        return "Yes"
                    else:
                        return "No"
            else:
                return "No"
    else:
        return "No"


