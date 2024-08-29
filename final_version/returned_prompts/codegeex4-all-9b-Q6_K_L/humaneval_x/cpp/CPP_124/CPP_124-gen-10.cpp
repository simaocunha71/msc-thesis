#include <string>
#include <vector>

using namespace std;

class Date {
public:
    Date(int year, int month, int day) : year(year), month(month), day(day) {}

    bool isValid() const {
        // Check if the year is valid
        if (year < 1 || year > 9999) {
            return false;
        }

        // Check if the month is valid
        if (month < 1 || month > 12) {
            return false;
        }

        // Check if the day is valid for the given month
        if (day < 1 || day > getDaysInMonth()) {
            return false;
        }

        return true;
    }

private:
    int year;
    int month;
    int day;

    int getDaysInMonth() const {
        if (month == 2) {
            // Check for leap year
            if (isLeapYear()) {
                return 29;
            } else {
                return 28;
            }
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            return 30;
        } else {
            return 31;
        }
    }

    bool isLeapYear() const {
        if (year % 4 != 0) {
            return false;
        } else if (year % 100 != 0) {
            return true;
        } else if (year % 400 != 0) {
            return false;
        } else {
            return true;
        }
    }
};

bool isValidDate(const string& date) {
    if (date.empty()) {
        return false;
    }

    // Split the date string into year, month, and day
    vector<string> parts;
    string part;
    for (char c : date) {
        if (c == '-') {
            parts.push_back(part);
            part.clear();
        } else {
            part += c;
        }
    }
    parts.push_back(part);

    // Check if the date string has the correct format
    if (parts.size() != 3) {
        return false;
    }

    // Convert the parts to integers
    int year, month, day;
    try {
        year = stoi(parts[0]);
        month = stoi(parts[1]);
        day = stoi(parts[2]);
    } catch (...) {
        return false;
    }

    // Create a Date object and check if it is valid
