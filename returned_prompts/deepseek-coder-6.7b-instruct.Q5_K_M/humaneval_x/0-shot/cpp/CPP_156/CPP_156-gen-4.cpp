    vector<string> roman = {"i", "iv", "v", "ix", "x", "xl", "l", "xc", "c", "cd", "d", "cm", "m"};
    vector<int> num = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
    string res = "";

B:
    for(int i=12; i>=0; i--){
        while(number>=num[i]){
            number -= num[i];
            res += roman[i];
        }
    }
    return res;
}

int main(){
    printf("%s", int_to_mini_roman(19).c_str());
    printf("%s", int_to_mini_roman(152).c_str());
    printf("%s", int_to_mini_roman(426).c_str());
    return 0;
}

*/

int main(){
    printf("%s", int_to_mini_roman(19).c_str());
    printf("%s", int_to_mini_roman(152).c_str());
    printf("%s", int_to_mini_roman(426).c_str());
    return 0;
}

//Problem_2/roman_numeral_decoder.cpp
/*
