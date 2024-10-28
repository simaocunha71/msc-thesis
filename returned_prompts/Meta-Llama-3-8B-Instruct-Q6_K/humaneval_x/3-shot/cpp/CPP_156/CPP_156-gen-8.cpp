    vector<string> roman_numerals = {"", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx"};
    vector<string> tens = {"", "", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc", "c", "cci", "ccc", "cd", "d", "dc", "dxc", "dcc", "dccc", "cm", "m", "mcci", "mc", "mcd", "m", "mmc", "mm", "mmcc", "mmcm", "mmccc", "mmcd", "m", "mmmm", "mmmm"};
    string result;
    if (number >= 1000) {
        int thousands = number / 1000;
        for (int i = 0; i < thousands; i++) {
            result += "m";
        }
        number %= 1000;
    }
    if (number >= 900) {
        result += "cm";
        number -= 900;
    }
    if (number >= 500) {
        result += "d";
        number -= 500;
    }
    if (number >= 400) {
        result += "cd";
        number -= 400;
    }
    for (int i = 0; i < number; i++) {
        result += tens[i % 10];
        if (i % 10 == 9) {
            result += tens[i / 10 + 1];
        }
    }
    return tolower(result);
}#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string int_to_mini_romank(int number){
    vector<string> roman_numerals = {"", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx"};
    vector<string> tens = {"", "", "xx", "xxx", "xl", "l", "lx