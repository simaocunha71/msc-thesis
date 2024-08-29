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
    map<string, int> m;
    string result;
    m["zero"] = 0;
    m["one"] = 1;
    m["two"] = 2;
    m["three"] = 3;
    m["four"] = 4;
    m["five"] = 5;
    m["six"] = 6;
    m["seven"] = 7;
    m["eight"] = 8;
    m["nine"] = 9;
    string temp;
    for(int i=0; i<numbers.size(); i++){
        if(numbers[i] == ' '){
            result += temp + ' ';
            temp.clear();
        }
        else{
            temp += numbers[i];
        }
    }
    result += temp;
    string res;
    for(int i=0; i<result.size(); i++){
        if(result[i] != ' '){
            res += result[i];
        }
        else{
            int a = m[res];
            int b = m[temp];
            if(a > b){
                res = temp;
            }
            temp.clear();
        }
    }
    return res;
}

B:
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
    map<string, int> m;
    string result;
    m["zero"] = 0;
    m["one"] = 1;
    m["two"] = 2;
    m["three"] = 3;
    m["four"] = 4;
    m["five"] = 5;
    m["six"] = 6