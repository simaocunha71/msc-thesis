    from datetime import datetime

    def valid_date(date):
        try:
            datetime.strptime(date, '%m-%d-%Y')
            return True
        except ValueError:
            return False

# test the function
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))  # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
print(valid_date(''))  # False
print(valid_date('13-13-2022'))  # False
print(valid_date('01-02-2023'))  # True
print(valid_date('02-30-2024'))  # False
print(valid_date('03-31-2025'))  # False
print(valid_date('04-31-2026'))  # False
print(valid_date('05-31-2027'))  # False
print(valid_date('06-31-2028'))  # False
print(valid_date('07-31-2029'))  # False
print(valid_date('08-31-2030'))  # False
print(valid_date('09-31-2031'))  # False
print(valid_date('10-31-2032'))  # False
print(valid_date('11-31-2033'))  # False
print(valid_date('12-31-2034'))  # True
print(valid_date('02-29-2032'))  # True
print(valid_date('02-30-2032'))  # False
print(valid_date('02-28-2032'))  # False
print(valid_date('02-27-2032'))  # False
print(valid_date('02-26-2032'))  # False
print(valid_date('02-25-2032'))  # False
print(valid_date('02-24-2032'))  # False
print(valid_date('02-23-2032'))  # False
print(valid_date('02-22-2032'))  # False
print(valid_date('02-21-2032'))  # False
print(valid_date('02-20-2032'))  # False
print(valid_date('02-19-2032'))  # False
print(valid_date('02-18-203