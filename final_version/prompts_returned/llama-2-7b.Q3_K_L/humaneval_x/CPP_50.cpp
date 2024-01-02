#include<stdio.h>
#include<string>
using namespace std;
string encode_shift(string s){
    // returns encoded string by shifting every character by 5 in the alphabet.
    string out;
    int i;
    for (i=0;i<s.length();i++)
    {
        int w=((int)s[i]+5-(int)'a')%26+(int)'a';   
        out=out+(char)w;
    }
    return out;
}
string decode_shift(string s){
    // takes as input string encoded with encode_shift function. Returns decoded string.
    int i,j;
    for (i=0;i<s.length();i++){
        for (j=0;j<26;j++){
            if ((int)(s[i]-'a')==j) break;
        }
        s=s.substr(1,i);
    }
    return s;
}
string reverse_shift(string x){
    // takes as input string encoded with encode_shift function and returns the inverse encoded version.
    int i;
    for (i=x.length()-1;i>=0;i--)
        x=reverse_shift(x.substr(0,i));
    
    return x;
}
int main(){
    char ch;
    string s="Hello World!";
    printf("Original String: %s\n",s.c_str());
    printf("Encoded String: %s\n",encode_shift(s).c_str());
    printf("Decoded String: %s\n",decode_shift(reverse_shift(encode_shift(s))).c_str());
}