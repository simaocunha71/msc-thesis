#include<stdio.h>
#include<string>
#include<openssl/md5.h>
#include<iostream>
using namespace std;
string string_to_md5(string text){
    if(text.length()==0){
        return NULL;
    }
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);
    char buffer[3];
    string md5string="";
    for(int i=0;i<MD5_DIGEST_LENGTH;i++){
        sprintf(buffer,"%02x",result[i]);
        md5string+=buffer;
    }
    return md5string;
}