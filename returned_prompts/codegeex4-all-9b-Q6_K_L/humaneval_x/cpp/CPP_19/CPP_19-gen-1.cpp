#include<stdio.h>
#include<string>
#include<map>
using namespace std;
string sort_numbers(string numbers){
    map<string,int> mp = { {"zero",0},{"one",1},{"two",2},{"three",3},{"four",4},{"five",5},{"six",6},{"seven",7},{"eight",8},{"nine",9} };
    string result="";
    string temp="";
    for(char c:numbers){
        if(c!=' '){
            temp+=c;
        }
        else{
            result+=to_string(mp[temp])+' ';
            temp="";
        }
    }
    result+=to_string(mp[temp]);
    return result;
}