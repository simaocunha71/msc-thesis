/*
Given a string 'text", return its md5 hash equivalent string.
If 'text" is an empty string, return None.

>>> string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"
*/
#include<stdio.h>
#include<string>
#include<openssl/md5.h>
using namespace std;
string string_to_md5(string text){
    if (text.empty())
        return "";
    MD5_CTX c;
    MD5_Init(&c);
    MD5_Update(&c, text.c_str(), text.size());
    unsigned char digest[16];
    MD5_Final(digest, &c);
    stringstream ss;
    for (int i = 0; i < 16; i++)
        ss << hex << setw(2) << setfill('0') << (int)digest[i];
    string md5str = ss.str();
    return md5str;
}
