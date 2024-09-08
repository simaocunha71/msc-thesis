    if(number > 0 && number <= 1000){
        string roman = "";
        vector<pair<int, string>> roman_numerals = {{1000, "m"}, {900, "cm"}, {500, "d"}, {400, "cd"}, {100, "c"}, {90, "xc"}, {50, "l"}, {40, "xl"}, {10, "x"}, {9, "ix"}, {5, "v"}, {4, "iv"}, {1, "i"}};

        for(auto numeral : roman_numerals){
            while(number >= numeral.first){
                roman += numeral.second;
                number -= numeral.first;
            }
        }
        return roman;
    }
    else{
        printf("Invalid number range\n");
        return "";
    }
}
int main() {
    printf("%s\n",int_to_mini_romank(19).c_str());
    printf("%s\n",int_to_mini_romank(152).c_str());
    printf("%s\n",int_to_mini_romank(426).c_str());
    return 0;
}

Answer:
Here is the corrected code:

```c
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

string int_to_mini_romank(int number) {
    if(number > 0 && number <= 1000){
        string roman = "";
        vector<pair<int, string>> roman_numerals = {{1000, "m"}, {900, "cm"}, {500, "d"}, {400, "cd"}, {100, "c"}, {90, "xc"}, {50, "l"}, {40, "xl"}, {10, "x"}, {9, "ix"}, {5, "v"}, {4, "iv"}, {1, "i"}};

        for(auto numeral : roman_numerals){
            while(number >= numeral.first){
                roman += numeral.second;
                number -= numeral.first;
            }
        }
        return roman;
    }
    else{
        printf("Invalid number range\n");
        return "";
    }
}

int main() {
    printf("%s\n",int_to_mini_romank(19).c_str());
    printf("%s\n",int_to_mini_romank(152).c_str());
    printf("%s\n",int_to_mini_romank(426).c_str());
    return 0;
}
```

Explanation:

1.  The function `int_to_mini_romank` takes an integer as input and returns its Roman numeral equivalent