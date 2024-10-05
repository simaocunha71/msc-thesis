    def valid_date(date):
        months = ["01", "03", "05", "07", "08", "10", "12"]
        for m in months:
            if date.find(m) == -1:
                return False
        if len(date.split("-")) != 3:
            return False
        m, d, y = date.split("-")
        if int(d) > 31:
            return False
        if int(m) > 12:
            return False
        if int(m) == 2 and int(d) > 28:
            return False
        if (int(m) in months and int(d) > 30):
            return False
        if (int(y) % 4 == 0 and int(m) == "02" and int(d) > 29):
            return False
        return True


