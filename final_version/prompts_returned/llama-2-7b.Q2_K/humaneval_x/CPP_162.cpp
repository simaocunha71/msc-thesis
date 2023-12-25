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
	unsigned char result[16];
	MD5 m;
    strcspn(text.c_str(), "\0", 16);

	int i = 0, j = 0;
    while (i < 16) {
        j = i + ((strlen(&text[j]) - 1));
        result[i] = (unsigned char)strtol((char*)&text[j], NULL);
        i++;
    }
    sprintf(result, "%02x", m.final(result));
    return string("");
}
