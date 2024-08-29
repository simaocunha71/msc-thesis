bool isLeapYear(int year)
{
    if (year % 4 == 0)
    {
        if (year % 100 == 0)
        {
            if (year % 400 == 0)
                return true;
            else
                return false;
        }
        else
            return true;
    }
    else
        return false;
}

bool valid_date(string date) {
    // Check if the date is empty
    if(date.empty()) {
        return false;
    }

    // Check if the date is in the format mm-dd-yyyy
    if(date.length() != 10 || date[2] != '-' || date[5] != '-') {
        return false;
    }

    // Extract the month, day, and year from the date string
    int month = stoi(date.substr(0, 2));
    int day = stoi(date.substr(3, 2));
    int year = stoi(date.substr(6, 4));

    // Check if the year, month, and day are valid
    if(year < 1 || month < 1 || day < 1) {
        return false;
    }

    // Check if the month and day are valid for the given year
    if(month > 12 || (month == 2 && (day > 29 || (day > 28 && !isLeapYear(year)))) || (month == 4 || month == 6 || month == 9 || month == 11) && day > 30) {
        return false;
    }

    // If all checks pass, the date is valid
    return true;
}

int main() {
    printf("%d\n", valid_date("03-11-2000")); // true
    printf("%d\n", valid_date("15-01-2012")); // false
    printf("%d\n", valid_date("04-0-2040")); // false
    printf("%d\n", valid_date("06-04-2020")); // true
    printf("%d\n", valid_date("06/04/2020")); // false

    return 0;
}

