    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> numerals = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};

    string result = "";

    for(int i=0; i<values.size(); i++){
        while(number >= values[i]){
            number -= values[i];
            result += numerals[i];
        }
    }

    return result;
}
int main() {
    int n;
    printf("Enter a number to convert to roman numeral: ");
    scanf("%d",&n);
    printf("%s", int_to_mini_roman(n).c_str());
    return 0;
}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string int_to_mini_roman(int num){

    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> numerals = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};

    string result = "";

    for(int i=0; i<values.size(); i++){
        while(num >= values[i]){
            num -= values[i];
            result += numerals[i];
        }
    }

    return result;
}
int main() {
    int n;
    printf("Enter a number to convert to roman numeral: ");
    scanf("%d",&n);
    printf("%s", int