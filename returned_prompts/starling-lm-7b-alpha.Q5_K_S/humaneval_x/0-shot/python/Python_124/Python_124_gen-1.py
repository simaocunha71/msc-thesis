    def valid_date(date):
        if len(date) == 0:
            return False
        date_parts = date.split('-')

        if len(date_parts) != 3:
            return False

        if not date_parts[0].isdigit() or not date_parts[1].isdigit() or not date_parts[2].isdigit():
            return False

        day = int(date_parts[1])
        month = int(date_parts[0])
        year = int(date_parts[2])

        if month > 12 or month < 1:
            return False

        if day > 31 or day < 1:
            if month not in [1, 3, 5, 7, 8, 10, 12]:
                return False

        if day > 30 or day < 1:
            if month not in [4, 6, 9, 11]:
                return False

        if day > 29 or day < 1:
            if month != 2:
                return False

        if year > 2020 or year < 0:
            return False

        return True


# Test
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))  # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False












































































































