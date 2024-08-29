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
    string result="";
    int a_len=a.length();
    int b_len=b.length();
    int max_len=a_len>b_len?a_len:b_len;
    for(int i=0;i<max_len;i++){
        if(a[i]=='1'&&b[i]=='1') result+="0";
        else if(a[i]=='0'&&b[i]=='0') result+="0";
        else result+="1";
    }
    return result;
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
    string result="";
    int a_len=a.length();
    int b_len=b.length();
    int max_len=a_len>b_len?a_len:b_len;
    for(int i=0;i<max_len;i++){
        if(a[i]=='1'&&b[i]=='1') result+="0";
        else if(a[i]=='0'&&b[i]=='0') result+="0";
        else result+="1";
    }
    return result;
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
    string result="";
    int a_len=a.length();
    int b_len=b.length();
    int max_len=a_len>b_len?a_len:b_len;
    for(int i=0;i<max_len;i++){
        if(a[i]=='1'&&b[i]=='1') result+="0";
        else if(a[i]=='0'&&b[i]=='0') result+="0";
        else result+="1";
    }
    return result;
}

D:
/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also