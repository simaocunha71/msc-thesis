/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string filp_case(string str){
    string ans="";
    for(int i=0;i<str.length();i++){
        if(islower(str[i])){
            ans+=str[i]-32;
        }
        else{
            ans+=str[i]+32;
        }
    }
    return ans;
}