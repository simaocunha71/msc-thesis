/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor("010", "110")
"100"
*/
#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    string c;
    int i,j;
    for(i=0;i<a.size();i++){
        for(j=0;j<b.size();j++){
            if(a[i]==b[j])
                c.push_back('0');
            else
                c.push_back('1');
        }
    }
    return c;
}
/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor("010", "110")
"100"
*/
#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    string c;
    int i,j;
    for(i=0;i<a.size();i++){
        for(j=0;j<b.size();j++){
            if(a[i]==b[j])
                c.push_back('0');
            else
                c.push_back('1');
        }
    }
    return c;
}
