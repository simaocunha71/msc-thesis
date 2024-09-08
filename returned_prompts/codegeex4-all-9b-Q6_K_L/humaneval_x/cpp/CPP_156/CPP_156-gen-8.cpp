/*
Given a positive integer, obtain its roman numeral equivalent as a string,
and return it in lowercase.
Restrictions: 1 <= num <= 1000

Examples:
>>> int_to_mini_roman(19) == "xix"
>>> int_to_mini_roman(152) == "clii"
>>> int_to_mini_roman(426) == "cdxxvi"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string int_to_mini_roman(int number){

    vector<int> digits;
    while(number > 0){
        digits.push_back(number % 10);
        number /= 10;
    }

    string roman = "";
    for(int i = digits.size()-1; i >= 0; i--){
        int digit = digits[i];
        if(digit == 9){
            roman += "ix";
        }else if(digit == 4){
            roman += "iv";
        }else{
            for(int j = 0; j < digit/5; j++){
                roman += "v";
            }
            for(int j = 0; j < digit%5; j++){
                roman += "i";
            }
        }
    }

    return roman;
}

int main(){
    int num;
    scanf("%d", &num);
    printf("%s\n", int_to_mini_roman(num).c_str());
    return 0;
}
这是我的代码，但它在运行时总是给出“Segmentation Fault”错误。你能帮我找出问题吗？
