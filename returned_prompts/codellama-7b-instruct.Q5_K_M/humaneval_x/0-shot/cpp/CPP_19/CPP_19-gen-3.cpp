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

    stringstream ss(numbers);
    string number;
    map<string, int> m;
    while(getline(ss, number, ' ')){
        m[number]++;
    }

    vector<pair<string, int>> vec;
    for(auto it = m.begin(); it != m.end(); it++){
        vec.push_back(*it);
    }
    sort(vec.begin(), vec.end(), [](const pair<string, int>& a, const pair<string, int>& b){
        return a.second < b.second;
    });
    string res;
    for(auto it = vec.begin(); it != vec.end(); it++){
        res += it->first;
        res += ' ';
    }
    return res;
}


int main(){
    string numbers = "three one five";
    string sorted = sort_numbers(numbers);
    printf("%s\n", sorted.c_str());
    return 0;
}
