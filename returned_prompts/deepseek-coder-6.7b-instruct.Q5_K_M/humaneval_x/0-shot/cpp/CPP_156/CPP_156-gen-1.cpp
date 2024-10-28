    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> numerals = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    string result = "";

B:
    for (int i=0; i<values.size(); i++){
        while (number >= values[i]){
            number -= values[i];
            result += numerals[i];
        }
    }

C:
    return result;
}

int main(){

D:
    printf("%s\n", int_to_mini_romank(19).c_str());
    printf("%s\n", int_to_mini_romank(152).c_str());
    printf("%s\n", int_to_mini_romank(426).c_str());

E:
    return 0;
}

*/


#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string int_to_mini_roman(int number){

    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> numerals = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    string result = "";

    for (int i=0; i<values.size(); i++){
        while (number >= values[i]){
            number -= values[i];
            result += numerals[i];
        }
    }

    return result;
}

