    if(text.empty()) return "";
    string result;
    MD5_CTX md5;
    MD5_Init(&md5);
    MD5_Update(&md5, text.c_str(), text.length());
    unsigned char digest[16];
    MD5_Final(digest, &md5);
    for(int i = 0; i < 16; i++){
        result += sprintf("%02x", digest[i]);
    }
    return result;
}

*/

#include<stdio.h>
#include<string>
#include<openssl/md5.h>
using namespace std;
string string_to_md5(string text){
    if(text.empty()) return "";
    string result;
    MD5_CTX md5;
    MD5_Init(&md5);
    MD5_Update(&md5, text.c_str(), text.length());
    unsigned char digest[16];
    MD5_Final(digest, &md5);
    for(int i = 0; i < 16; i++){
        result += sprintf("%02x", digest[i]);
    }
    return result;
}

*/

#include<stdio.h>
#include<string>
#include<openssl/md5.h>
using namespace std;
string string_to_md5(string text){
    if(text.empty()) return "";
    string result;
    MD5_CTX md5;
    MD5_Init(&md5);
    MD5_Update(&md5, text.c_str(), text.length());
    unsigned char digest[16];
    MD5_Final(digest, &md5);
    for(int i = 0; i < 16; i++){
        result += sprintf("%02x", digest[i]);
    }
    return result;
}

*/

#include<stdio.h>
#include<string>
#include<openssl/md5.h>
using namespace std;
string string_to_md5(string text){
    if(text.empty()) return "";
   