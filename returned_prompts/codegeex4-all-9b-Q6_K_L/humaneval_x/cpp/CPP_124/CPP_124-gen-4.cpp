#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool isLeapYear(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

bool isValidDate(int day, int month, int year) {
    if (day < 1 || day > 31) return false;
    if (month < 1 || month > 12) return false;
    if (month == 2) {
        if (isLeapYear(year)) {
            return (day <= 29);
        } else {
            return (day <= 28);
        }
    } else if (month == 4 || month == 6 || month == 9 || month == 11) {
        return (day <= 30);
    }
    return true;
}

bool valid_date(string date) {
    stringstream ss(date);
    vector<string> parts;
    string part;
    while (getline(ss, part, '-')) {
        parts.push_back(part);
    }
    
    if (parts.size() != 3) return false;
    
    int month, day, year;
    try {
        month = stoi(parts[0]);
        day = stoi(parts[1]);
        year = stoi(parts[2]);
    } catch (invalid_argument) {
        return false;
    }
    
    return isValidDate(day, month, year);
}

int main() {
    cout << valid_date("03-11-2000") << endl; // true
    cout << valid_date("15-01-2012") << endl; // false
    cout << valid_date("04-0-2040") << endl; // false
    cout << valid_date("06-04-2020") << endl; // true
    cout << valid_date("06/04/2020") << endl; // false
    return 0;
}
B:
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool isLeapYear(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

bool isValidDate(int day, int month, int year) {
    if (day < 1 || day > 31) return false;
    if (month < 1 || month > 12) return false;
   