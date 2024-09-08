    vector<pair<int, string>> roman = {{1000, "m"}, {900, "cm"}, {500, "d"}, {400, "cd"}, {100, "c"}, {90, "xc"}, {50, "l"}, {40, "xl"}, {10, "x"}, {9, "ix"}, {5, "v"}, {4, "iv"}, {1, "i"}};
    string res = "";
    for (int i = 0; i < roman.size(); i++) {
        while (number >= roman[i].first) {
            number -= roman[i].first;
            res += roman[i].second;
        }
    }
    return res;
}

int main() {
    printf("%s\n", int_to_mini_romank(19).c_str());
    printf("%s\n", int_to_mini_romank(152).c_str());
    printf("%s\n", int_to_mini_romank(426).c_str());
    return 0;
}

C:
#include <stdio.h>

char* int_to_roman(int num) {
    char* res = (char*)malloc(10000);
    res[0] = '\0';
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    char* roman[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int i = 0;
    while (num > 0) {
        if (num >= values[i]) {
            num -= values[i];
            strcat(res, roman[i]);
        } else {
            i++;
        }
    }
    return res;
}

int main() {
    printf("%s\n", int_to_roman(19));
    printf("%s\n", int_to_roman(152));
    printf("%s\n", int_to_roman(426));
    return 0;
}
E:
```
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM