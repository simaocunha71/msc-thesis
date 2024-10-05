    def days_in_month(m, y):
        if m == 2:
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                return 29
            else:
                return 28
        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            return 31
        else:
            return 30

    parts = date.split('-')
    if len(parts) != 3:
        return False

    if parts[0] == "" or parts[1] == "" or parts[2] == "":
        return False

    if not parts[0].isdigit() or not parts[1].isdigit() or not parts[2].isdigit():
        return False

    if int(parts[0]) < 1 or int(parts[0]) > 12:
        return False

    if int(parts[1]) < 1 or int(parts[1]) > days_in_month(int(parts[0]), int(parts[2][:4])):
        return False

    if int(parts[2][:4]) < 0 or len(parts[2]) != 4:
        return False

    return True


