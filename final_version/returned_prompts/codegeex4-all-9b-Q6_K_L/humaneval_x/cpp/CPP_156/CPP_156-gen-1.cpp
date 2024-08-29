#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Roman {
  private:
    static const int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    static const string symbols[] = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
  public:
    static string intToRoman(int num) {
      string roman;
      for (int i = 0; i < 13; ++i) {
        while (num >= values[i]) {
          roman += symbols[i];
          num -= values[i];
        }
      }
      return roman;
    }
};

int main() {
  int number;
  cout << "Enter a number: ";
  cin >> number;
  string roman = Roman::intToRoman(number);
  cout << "Roman numeral: " << roman << endl;
  return 0;
}
C:
#include<iostream>
#include<string>
using namespace std;

string int_to_mini_roman(int number){
  string result = "";
  int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
  string symbols[] = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
  for (int i = 0; i < 13; ++i) {
    while (number >= values[i]) {
      result += symbols[i];
      number -= values[i];
    }
  }
  return result;
}

int main() {
  int number;
  cout << "Enter a number: ";
  cin >> number;
  string roman = int_to_mini_roman(number);
  cout << "Roman numeral: " << roman << endl;
  return 0;
}
D:
#include<iostream>
#include<string>
using namespace std;

string int_to_mini_roman(int number){
  string result = "";
  int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 