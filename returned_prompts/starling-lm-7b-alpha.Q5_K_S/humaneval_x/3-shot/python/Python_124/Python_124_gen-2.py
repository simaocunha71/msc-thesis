    def valid_date(date):
        date_list = date.split("-")
        if len(date_list) != 3 or date_list[0] == "" or date_list[1] == "" or date_list[2] == "":
            return False
        months = [1, 3, 5, 7, 8, 10, 12]
        if int(date_list[0]) not in range(1, 13) or int(date_list[1]) not in range(1, 32):
            return False
        if date_list[0] == "2" and int(date_list[1]) > 29:
            return False
        for month in months:
            if int(date_list[0]) == month and int(date_list[1]) > 31:
                return False
        return True


