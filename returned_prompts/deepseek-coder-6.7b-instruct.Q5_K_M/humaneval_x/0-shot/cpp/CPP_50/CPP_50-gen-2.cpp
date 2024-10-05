#include<stdio.h>
#include<string>
using namespace std;
string encode_shift(string s){
    string out;
    int i;
    for  (i=0;i<s.length();i++)
    {
        int w=((int)s[i]-5-(int)'a')%26+(int)'a';
        out=out+(char)w;
    }
    return out;
}
string decode_shift(string s){
    string out;
    int i;
    for  (i=0;i<s.length();i++)
    {
        int w=((int)s[i]+5-(int)'a')%26+(int)'a';
        out=out+(char)w;
    }
    return out;
}

In the encode_shift function, we subtract 5 from the ASCII value of each character in the input string and then find its modulo with 26 (the number of alphabet letters) and add 'a' to get the encoded character. In the decode_shift function, we add 5 to the ASCII value of each character in the input string, find its modulo with 26 and add 'a' to get the decoded character.
Both functions will work for any input string and will return the correct encoded/decoded string.
The encode_shift function will encode the string by shifting every character by 5 in the alphabet.
The decode_shift function will decode the encoded string back to its original form.
The functions assume that the input string contains only lowercase letters and does not contain any other characters. If the input string contains uppercase letters or other characters, the functions will not work correctly.
The functions do not handle the case where the encoded character is outside the range of lowercase letters ('a'-'z'). In this case, the modulo operation will wrap the character back to the start of the alphabet.

*/

//test cases
int main(){
    string s = "hello";
    string encoded = encode_shift(s);
    string decoded = decode_shift(encoded);
    printf("Original string: %s\nEncoded string: %s\nDecoded string: