    if date == "":
        return False
    else:
        if date.count("-") != 2:
            return False
        else:
            date_list = date.split("-")
            if int(date_list[0]) < 1 or int(date_list[0]) > 12:
                return False
            elif int(date_list[1]) < 1 or int(date_list[1]) > 31:
                return False
            elif int(date_list[2]) < 1 or int(date_list[2]) > 9999:
                return False
            else:
                if int(date_list[0]) in [1, 3, 5, 7, 8, 10, 12]:
                    if int(date_list[1]) < 1 or int(date_list[1]) > 31:
                        return False
                elif int(date_list[0]) in [4, 6, 9, 11]:
                    if int(date_list[1]) < 1 or int(date_list[1]) > 30:
                        return False
                elif int(date_list[0]) == 2:
                    if int(date_list[1]) < 1 or int(date_list[1]) > 29:
                        return False
                else:
                    return True


