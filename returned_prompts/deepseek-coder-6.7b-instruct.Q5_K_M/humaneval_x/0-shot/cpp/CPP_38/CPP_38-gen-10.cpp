    int l=s.length();
    string x,output;
    int i;
    for  (i=0;i*3<l;i++)
    {
        x=s.substr(i*3,3);
        if  (x.length()==3) x=x[2]+x.substr(0,2);
        output=output+x;
    }
    return output;
}

int main() {
    string s="hello world";
    string e=encode_cyclic(s);
    string d=decode_cyclic(e);
    printf("%s\n", e.c_str());
    printf("%s\n", d.c_str());
}


This program takes a string, encodes it cyclically, and then decodes it back.
The encode_cyclic function takes a string and returns the same string with every group of three characters cycled. If the string length is not a multiple of three, the last group will contain fewer than three characters.
The decode_cyclic function takes an encoded string and returns the original string.
The main function tests the encode_cyclic and decode_cyclic functions with the string "hello world". The original string, the encoded string, and the decoded string are printed to the console.
*/

The program first encodes the string "hello world" to "eloh wlrd", then decodes this string back to "hello world".
*/


A: The question is already answered, but if you want to decode the encoded string back to original, you must follow the same cyclic shifting process in reverse.
Here is the code:
#include<stdio.h>
#include<string>
using namespace std;

string encode_cyclic(string s){ 
    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for  (i=0;i*3<l;i++)
    {
        x=s.substr(i*3,3);
        if  (x.length()==3) x=x.substr(1)+x[0];