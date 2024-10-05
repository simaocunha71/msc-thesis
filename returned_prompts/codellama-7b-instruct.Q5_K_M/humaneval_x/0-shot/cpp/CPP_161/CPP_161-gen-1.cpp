/*
You are given a string s.
if s[i] is a letter, reverse its case from lower to upper or vise versa, 
otherwise keep it as it is.
If the string contains no letters, reverse the string.
The function should return the resulted string.
Examples
solve("1234") = "4321"
solve("ab") = "AB"
solve("#a@C") = "#A@c"
*/
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){

    int len = s.size();
    string out;
    for(int i = 0; i < len; i++){
        if(s[i] >= 'a' && s[i] <= 'z')
            out += (char)(s[i] - 32);
        else if(s[i] >= 'A' && s[i] <= 'Z')
            out += (char)(s[i] + 32);
        else
            out += s[i];
    }
    return out;
}

