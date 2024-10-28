    from datetime import datetime

    def valid_date(date):
        try:
            datetime.strptime(date, '%m-%d-%Y')
            return True
        except ValueError:
            return False
    # test cases
    print(valid_date('03-11-2000'))  # True
    print(valid_date('15-01-2012'))  # False
    print(valid_date('04-0-2040'))  # False
    print(valid_date('06-04-2020'))  # True
    print(valid_date('06/04/2020'))  # False
    # test case with invalid date format
    print(valid_date('2000-01-01'))  # False
    print(valid_date('30-02-2000'))  # False
    print(valid_date('13-13-2020'))  # False
    print(valid_date(''))  # False
    print(valid_date('12-40-2020'))  # False
    print(valid_date('12-30-2020'))  # False
    print(valid_date('02-29-2020'))  # False
    print(valid_date('02-30-2020'))  # False
    print(valid_date('02-28-2020'))  # True
    print(valid_date('02-27-2020'))  # True
    print(valid_date('02-26-2020'))  # True
    print(valid_date('02-25-2020'))  # True
    print(valid_date('02-24-2020'))  # True
    print(valid_date('02-23-2020'))  # True
    print(valid_date('02-22-2020'))  # True
    print(valid_date('02-21-2020'))  # True
    print(valid_date('02-20-2020'))  # True
    print(valid_date('02-19-2020'))  # True
    print(valid_date('02-18-2020'))  # True
    print(valid_date('02-17-2020'))  # True
    print(valid_date('02-16-2020'))  # True
    print(valid_date('02-15-2020'))  # True
    print(valid_date('02-14-2020'))  # True
    print(valid_date('02-13-2020'))  # True
   