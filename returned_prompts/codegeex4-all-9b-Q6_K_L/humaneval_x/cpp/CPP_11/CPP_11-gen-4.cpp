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
    string result="";
    if(a.size()>b.size()){
        int diff=a.size()-b.size();
        for(int i=0;i<diff;i++)
            b="0"+b;
    }
    else{
        int diff=b.size()-a.size();
        for(int i=0;i<diff;i++)
            a="0"+a;
    }
    for(int i=0;i<a.size();i++){
        int temp=a[i]-48;
        int temp1=b[i]-48;
        if(temp==temp1)
            result=result+"0";
        else
            result=result+"1";
    }
    return result;

B:
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
    string result="";
    if(a.size()>b.size()){
        int diff=a.size()-b.size();
        for(int i=0;i<diff;i++)
            b="0"+b;
    }
    else{
        int diff=b.size()-a.size();
        for(int i=0;i<diff;i++)
            a="0"+a;
    }
    for(int i=0;i<a.size();i++){
        int temp=a[i]-48;
        int temp1=b[i]-48;
        if(temp==temp1)
            result=result+"0";
        else
            result=result+"1";
    }
    return result;
}
请问，哪个代码是正确的？

A和B的代码都是正确的。它们都实现了将两个字符串形式的二进制数进行异或操作，并返回结果字符串的功能。两个代码的主要区别在于它们在字符串长度不一致时，如何处理。

A的代码在处理字符串长度不一致时，先判断哪个字符串长，然后使用循环在较短的字符串前面添加零，使得两个字符串长度一致。然后再进行异或操作。

B的代码在处理字符串长度不一致时，也是先判断哪个字符串长，然后使用循环在较短的字符串前面添加零，