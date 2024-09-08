    // your code here
    // split the date string into day, month and year
    int day, month, year;
    size_t pos1 = date.find('-');
    size_t pos2 = date.find('-', pos1 + 1);

    // extract day
    day = stoi(date.substr(0, pos1));

    // extract month
    month = stoi(date.substr(pos1 + 1, pos2 - pos1 - 1));

    // extract year
    year = stoi(date.substr(pos2 + 1));

    // check if date is valid
    if (day < 1 || day > 31 || month < 1 || month > 12 || year < 1) {
        return false;
    }

    // check if month has 31 days
    if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
        if (day > 31) {
            return false;
        }
    }
    // check if month has 30 days
    else if (month == 4 || month == 6 || month == 9 || month == 11) {
        if (day > 30) {
            return false;
        }
    }
    // check if month has 29 days
    else if (month == 2) {
        if (day > 29) {
            return false;
        }
    }
    return true;
}
int main()
{
    cout<<valid_date("03-11-2000");
    return 0;
}
