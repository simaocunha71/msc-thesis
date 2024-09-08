    // split the string into three parts
    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    // Check if the date is in the correct format
    if (month.size() != 2 || day.size() != 2 || year.size() != 4) {
        return false;
    }

    // Convert the month and day to integers
    int m, d;
    if (sscanf_s(month.c_str(), "%d", &m) != 1 || sscanf_s(day.c_str(), "%d", &d) != 1) {
        return false;
    }

    // Check if the month and day are within valid ranges
    if (m < 1 || m > 12) {
        return false;
    }
    if (m == 2) {
        if (d < 1 || d > 29) {
            return false;
        }
    } else if (m == 4 || m == 6 || m == 9 || m == 11) {
        if (d < 1 || d > 30) {
            return false;
        }
    } else {
        if (d < 1 || d > 31) {
            return false;
        }
    }

    return true;
}

int main() {
    cout << valid_date("03-11-2000"); // true
    cout << endl;
    cout << valid_date("15-01-2012"); // false
    cout << endl;
    cout << valid_date("04-0-2040"); // false
    cout << endl;
    cout << valid_date("06-04-2020"); // true
    cout << endl;
    cout << valid_date("06/04/2020"); // false
    return 0;
}

B:
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

bool valid_date(const string& date) {
    string month, day, year;
    size_t pos = date.find('-');

    if (pos == string::npos)
        return false;

    month = date.substr(0, pos);
    day = date.substr(pos + 1, pos - date.find('-') - 1);
    year = date.substr(pos + 3);

    if (month.size() != 2 || day