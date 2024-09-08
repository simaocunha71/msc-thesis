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
    map<string, int> m = {{"zero",0},{"one",1},{"two",2},{"three",3},{"four",4},{"five",5},{"six",6},{"seven",7},{"eight",8},{"nine",9}};
    string result="";
    vector<string> v;
    stringstream s(numbers);
    string tmp;
    while(getline(s,tmp,' ')){
        v.push_back(tmp);
    }
    sort(v.begin(),v.end(),[&](const string& a, const string& b){
        return m[a]<m[b];
    });
    for(auto i:v){
        result+=i+" ";
    }
    return result.substr(0,result.length()-1);
}
int main(){
    printf("%s",sort_numbers("three one five").c_str());
    return 0;
}

