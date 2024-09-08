#include <iostream>
#include <string>

using namespace std;

bool valid_date(string date) {
  // Check if the date string is empty
  if (date.empty()) {
    return false;
  }

  // Check if the date string has the correct format
  if (date.length() != 10 || date[2] != '-' || date[5] != '-') {
    return false;
  }

  // Extract the month, day, and year from the date string
  int month = stoi(date.substr(0, 2));
  int day = stoi(date.substr(3, 2));
  int year = stoi(date.substr(6, 4));

  // Check if the month is valid
  if (month < 1 || month > 12) {
    return false;
  }

  // Check if the day is valid
  if (day < 1 || day > 31) {
    return false;
  }

  // Check if the year is valid
  if (year < 1 || year > 9999) {
    return false;
  }

  // Check if the day is valid for the given month and year
  if (month == 2) {
    bool is_leap_year = (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
    if (day > (is_leap_year ? 29 : 28)) {
      return false;
    }
  } else if (month == 4 || month == 6 || month == 9 || month == 11) {
    if (day > 30) {
      return false;
    }
  }

  // If all checks pass, the date is valid
  return true;
}

int main() {
  // Test cases
  cout << valid_date("03-11-2000") << endl;  // true
  cout << valid_date("15-01-2012") << endl;  // false
  cout << valid_date("04-0-2040") << endl;   // false
  cout << valid_date("06-04-2020") << endl;  // true
  cout << valid_date("06/04/2020") << endl;  // false

  return 0;
}