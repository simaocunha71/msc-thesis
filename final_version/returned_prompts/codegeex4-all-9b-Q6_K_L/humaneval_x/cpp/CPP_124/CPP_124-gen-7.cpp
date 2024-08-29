#include <iostream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

bool valid_date(string date){
    map<int, int> days_in_month;
    days_in_month[1] = 31;
    days_in_month[3] = 31;
    days_in_month[5] = 31;
    days_in_month[7] = 31;
    days_in_month[8] = 31;
    days_in_month[10] = 31;
    days_in_month[4] = 30;
    days_in_month[6] = 30;
    days_in_month[9] = 30;
    days_in_month[11] = 30;
    days_in_month[2] = 29;

    stringstream ss(date);
    vector<string> tokens;
    string token;
    while (getline(ss, token, '-')) {
        tokens.push_back(token);
    }

    if (tokens.size() != 3) {
        return false;
    }

    int month, day, year;
    try {
        month = stoi(tokens[0]);
        day = stoi(tokens[1]);
        year = stoi(tokens[2]);
    } catch (exception &e) {
        return false;
    }

    if (month < 1 || month > 12) {
        return false;
    }

    if (day < 1 || day > days_in_month[month]) {
        return false;
    }

    return true;
}

int main() {
    cout << valid_date("03-11-2000") << endl; // true
    cout << valid_date("15-01-2012") << endl; // false
    cout << valid_date("04-0-2040") << endl; // false
    cout << valid_date("06-04-2020") << endl; // true
    cout << valid_date("06/04/2020") << endl; // false
    return 0;
}

C:
#include <iostream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

bool valid_date(string date) {
    map<int, int> days_in_month;
    days_in_month[1] = 31;
    days_in_month[3] = 31;
    days_in_month[5] = 31;
    days_in_month[7] = 31;
    days_in_month[8] = 31;
    days_in_month[10]