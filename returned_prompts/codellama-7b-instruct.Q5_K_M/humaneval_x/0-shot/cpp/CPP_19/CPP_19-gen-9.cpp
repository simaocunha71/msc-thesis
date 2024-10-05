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

    map<string, int> n;
    n["zero"] = 0;
    n["one"] = 1;
    n["two"] = 2;
    n["three"] = 3;
    n["four"] = 4;
    n["five"] = 5;
    n["six"] = 6;
    n["seven"] = 7;
    n["eight"] = 8;
    n["nine"] = 9;
    vector<string> v;
    stringstream ss(numbers);
    string s;
    while(getline(ss, s, ' ')){
        v.push_back(s);
    }
    sort(v.begin(), v.end(), [&](string s1, string s2){
        return n[s1] < n[s2];
    });
    return string(v.begin(), v.end());
}

int main(){
    string numbers;
    getline(cin, numbers);
    printf("%s", sort_numbers(numbers).c_str());
}
