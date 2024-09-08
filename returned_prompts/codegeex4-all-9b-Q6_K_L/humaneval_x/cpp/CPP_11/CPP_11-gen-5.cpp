/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor("010", "110")
"100"
*/
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    string s="";
    int i=0;
    while(a[i]!='\0' || b[i]!='\0')
    {
        if(a[i]=='1' && b[i]=='1')
            s=s+'0';
        else if(a[i]=='0' && b[i]=='0')
            s=s+'0';
        else
            s=s+'1';
        i++;
    }
    return s;
}

B:
/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor("010", "110")
"100"
*/
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    string s="";
    int i=0;
    while(a[i]!='\0' || b[i]!='\0')
    {
        if(a[i]=='1' && b[i]=='1')
            s=s+'1';
        else if(a[i]=='0' && b[i]=='0')
            s=s+'0';
        else
            s=s+'1';
        i++;
    }
    return s;
}

C:
/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor("010", "110")
"100"
*/
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    string s="";
    int i=0;
    while(a[i]!='\0' || b[i]!='\0')
    {
        if(a[i]=='1' && b[i]=='1')
            s=s+'0';
        else if(a[i]=='0' && b[i]=='0')
            s=s+'0';
        else
            s=s+'1';
        i++;
    }
    return s;
}
D:
/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor("010", "110