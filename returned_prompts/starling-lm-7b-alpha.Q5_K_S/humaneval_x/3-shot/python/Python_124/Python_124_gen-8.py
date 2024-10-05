    def valid_date(date):
        month, day, year = date.split('-')
        if len(date) != 10 or len(month) != 2 or len(day) != 2 or len(year) != 4:
            return False
        months = ['01', '03', '05', '07', '08', '10', '12']
        if month in months:
            if int(day) > 31:
                return False
        elif month in ['04', '06', '09', '11']:
            if int(day) > 30:
                return False
        else:
            if int(day) > 29:
                return False
        months_valid = [month for month in range(1, 13) if month != '02' or int(day) <= 29]
        return month in months_valid


