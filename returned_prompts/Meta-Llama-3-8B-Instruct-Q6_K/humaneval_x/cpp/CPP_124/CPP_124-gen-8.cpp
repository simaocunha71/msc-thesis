    if(date.empty()) return false; // if the date string is empty, return false
    int month, day, year; // declare variables to store month, day, year
    if(sscanf(date.c_str(), "%d-%d-%d", &month, &day, &year)!=3) return false; // check if the date is in the correct format
    if(month<1 || month>12) return false; // check if the month is in the range 1-12
    if(year<1) return false; // check if the year is 1 or more
    if(month==2) { // if the month is february
        if(day<1 || day>29) return false; // check if the day is in the range 1-29
    }
    else if(month==4 || month==6 || month==9 || month==11) { // if the month is april, june, september, november
        if(day<1 || day>30) return false; // check if the day is in the range 1-30
    }
    else { // if the month is january, march, may, july, august, october, december
        if(day<1 || day>31) return false; // check if the day is in the range 1-31
    }
    return true; // if all checks pass, return true
}
int main() {
    cout << valid_date("03-11-2000") << endl; // returns true
    cout << valid_date("15-01-2012") << endl; // returns false
    cout << valid_date("04-0-2040") << endl; // returns false
    cout << valid_date("06-04-2020") << endl; // returns true
    cout << valid_date("06/04/2020") << endl; // returns false
    return 0;
}
B:
    string date="03-11-2000";
    bool result=valid_date(date);
    if(result) cout << "The date is valid";
    else cout << "The date is not valid";
    return 0;
}
C:
    int main() {
    cout << valid_date("03-11-2000") << endl; // returns true
    cout << valid_date("15-01-2012") << endl; // returns false
    cout << valid_date