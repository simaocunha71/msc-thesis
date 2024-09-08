/*
Input is a space-delimited string of numberals from "zero" to "nine".
Valid choices are "zero", "one", 'two", 'three", "four", "five", 'six", 'seven", "eight" and "nine".
Return the string with numbers sorted from smallest to largest
>>> sort_numbers('three one five")
"one three five"
*/
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
string sort_numbers(string numbers){

    map<string,int> str_num_map = {
        {"zero",0},
        {"one",1},
        {"two",2},
        {"three",3},
        {"four",4},
        {"five",5},
        {"six",6},
        {"seven",7},
        {"eight",8},
        {"nine",9}
    };

    map<int,string> num_str_map;
    for (auto& i : str_num_map){
        num_str_map[i.second] = i.first;
    }

    string result = "";

    int num = 0;
    string number = "";
    for (int i = 0; i < numbers.length(); i++){
        if (numbers[i] == ' '){
            if (number.length() > 0){
                num = str_num_map[number];
                result += num_str_map[num];
                result += " ";
                number = "";
            }
        } else {
            number += numbers[i];
        }
    }
    if (number.length() > 0){
        num = str_num_map[number];
        result += num_str_map[num];
    }
    return result;
}

int main(){
    string numbers = "three one five";
    string result = sort_numbers(numbers);
    printf("%s\n", result.c_str());
    return 0;
}
