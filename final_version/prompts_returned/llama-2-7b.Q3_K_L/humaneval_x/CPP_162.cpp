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
	MD5 md5;
	unsigned char digest[16];
    MD5((const unsigned char*)text.c_str(), strlen(text), (unsigned char *)digest);
  // return std::string(1, digest[0]);
   string temp = "";
for(int i=0;i<8;i++)
{
	if(((unsigned int)(digest[i])) < 16)
	{
	temp+= '0';
}
else
{
	temp+= (unsigned int)(digest[i])-16;
}
//return temp;
string str = (text +"").c_str();
return str.substr(0, 32);
}
