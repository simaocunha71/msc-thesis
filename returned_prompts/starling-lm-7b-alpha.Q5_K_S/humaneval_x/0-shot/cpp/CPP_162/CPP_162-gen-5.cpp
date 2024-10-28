    MD5_CTX md;
    MD5_Init(&md);
    MD5_Update(&md, text.c_str(), text.size());
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5_Final(result, &md);
    return string(reinterpret_cast<char *>(result), MD5_DIGEST_LENGTH);
}


/*
Given a string 'text", return its sha1 hash equivalent string.
If 'text" is an empty string, return None.

>>> string_to_sha1("Hello world") == "978f6c8913b33f0d5f0f3f3f6f6f3f6f6f6f3f6f"
*/
#include<stdio.h>
#include<string>
#include<openssl/sha.h>
using namespace std;
string string_to_sha1(string text){

B:
    SHA1_CTX ctx;
    SHA1_Init(&ctx);
    SHA1_Update(&ctx, text.c_str(), text.size());
    unsigned char result[SHA_DIGEST_LENGTH];
    SHA1_Final(result, &ctx);
    return string(reinterpret_cast<char *>(result), SHA_DIGEST_LENGTH);
}


/*
Given a string 'text", return its sha256 hash equivalent string.
If 'text" is an empty string, return None.

>>> string_to_sha256("Hello world") == "55804ed930300000000000000000000000000000000000000000000000000000"
*/
#include<stdio.h>
#include<string>
#include<openssl/sha.h>
using namespace std;
string string_to_sha256(string text){

C:
    SHA256_CTX ctx;
    SHA256_Init(&ctx);
    SHA256_Update(&ctx,