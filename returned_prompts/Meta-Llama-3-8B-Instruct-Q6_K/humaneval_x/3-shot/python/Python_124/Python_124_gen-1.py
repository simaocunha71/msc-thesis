    import re
    from datetime import datetime

    def valid_date(date):
        pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
        if not pattern.match(date):
            return False

        month, day, year = map(int, date.split('-'))
        if not 1 <= month <= 12:
            return False

        if month in [1, 3, 5, 7, 8, 10, 12]:
            if not 1 <= day <= 31:
                return False
        elif month in [4, 6, 9, 11]:
            if not 1 <= day <= 30:
                return False
        elif month == 2:
            if not 1 <= day <= 29:
                return False

        try:
            datetime(year, month, day)
        except ValueError:
            return False

        return True
    # test cases
    print(valid_date('03-11-2000'))  # True
    print(valid_date('15-01-2012'))  # False
    print(valid_date('04-0-2040'))  # False
    print(valid_date('06-04-2020'))  # True
    print(valid_date('06/04/2020'))  # False
    # output
    # True
    # False
    # False
    # True
    # False
    # end test cases
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code
    # end of your code