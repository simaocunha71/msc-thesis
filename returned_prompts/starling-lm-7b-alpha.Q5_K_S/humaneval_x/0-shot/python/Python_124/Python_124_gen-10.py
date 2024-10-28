
def valid_date(date):
    month, day, year = map(int, date.split('-'))
    if month < 1 or month > 12 or day < 1 or day > 31 or year < 0:
        return False
    if month in [2,4,6,9,11]:
        if day > 30:
            return False
    elif month == 2:
        if day > 28:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return True
            else:
                return False
    return True

# You can use the following main function to test your implementation

def main():
    print(valid_date('03-11-2000'))  # True
    print(valid_date('15-01-2012'))  # False
    print(valid_date('04-0-2040'))  # False
    print(valid_date('06-04-2020'))  # True
    print(valid_date('06/04/2020'))  # False

if __name__ == '__main__':
    main()


# This code is contributed by Siddharth



```
