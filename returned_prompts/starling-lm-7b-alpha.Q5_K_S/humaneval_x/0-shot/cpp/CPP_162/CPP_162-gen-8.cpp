    MD5_CTX context;
    MD5_Init(&context);
    MD5_Update(&context,text.c_str(),text.length());
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5_Final(digest,&context);
    string result;
    for(int i = 0; i < MD5_DIGEST_LENGTH; ++i){
        result += (char)digest[i];
    }
    return result;

}

*/
In this program,we are taking a string and converting it into a MD5 hash equivalent string.This program uses openssl library for MD5 hashing.
First we are creating a context using MD5_Init(&context).
Then we are updating the context with the given string using MD5_Update(&context,text.c_str(),text.length()).
After that we are creating a digest array of unsigned char using MD5_Final(digest,&context).
Then we are converting the digest array into a string and returning it.

*/
#include<stdio.h>
#include<string>
#include<openssl/md5.h>
using namespace std;
string string_to_md5(string text){

    MD5_CTX context;
    MD5_Init(&context);
    MD5_Update(&context,text.c_str(),text.length());
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5_Final(digest,&context);
    string result;
    for(int i = 0; i < MD5_DIGEST_LENGTH; ++i){
        result += (char)digest[i];
    }
    return result;

}

*/

In this program,we are taking a string and converting it into a MD5 hash equivalent string.This program uses openssl library for MD5 hashing.
First we are creating a context using MD5_Init(&context).
Then we are updating the context with the given string using MD5_Update(&context,text.c_str(),text.length()).
After that we are creating a digest array of unsigned char using MD5_Final(digest,&context).
Then we are converting the digest array into