    from datetime import datetime

    def valid_date(date):
        parts = date.split('-')
        if len(parts) != 3:
            return False
        month, day, year = map(int, parts)
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= 31):
            return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day > 31:
                return False
        elif month == 2:
            if day > 29:
                return False
        elif month in [4, 6, 9, 11]:
            if day > 30:
                return False
        try:
            datetime(int(year), int(month), int(day))
        except ValueError:
            return False
        return True
    # test the function
    print(valid_date('03-11-2000'))  # True
    print(valid_date('15-01-2012'))  # False
    print(valid_date('04-0-2040'))  # False
    print(valid_date('06-04-2020'))  # True
    print(valid_date('06/04/2020'))  # False
    # check for empty date
    print(valid_date(''))  # False
    # check for invalid date format
    print(valid_date('04-30-2040'))  # False
    print(valid_date('02-30-2040'))  # False
    print(valid_date('13-30-2040'))  # False
    print(valid_date('13-01-2040'))  # False
    print(valid_date('13-02-2040'))  # False
    print(valid_date('13-03-2040'))  # False
    print(valid_date('13-04-2040'))  # False
    print(valid_date('13-05-2040'))  # False
    print(valid_date('13-06-2040'))  # False
    print(valid_date('13-07-2040'))  # False
    print(valid_date('13-08-2040'))  # False
    print(valid_date('13-09-2040'))  # False
    print(valid_date('13-10-2040'))  # False
    print(valid_date('13-11-2040'))