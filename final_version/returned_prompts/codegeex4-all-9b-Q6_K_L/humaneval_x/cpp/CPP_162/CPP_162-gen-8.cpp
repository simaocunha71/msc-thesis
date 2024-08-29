```cpp
#include<stdio.h>
#include<string>
#include<openssl/md5.h>
using namespace std;
string string_to_md5(string text){
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.size(), (unsigned char*)&digest);
    char md5string[33];
    for(int i = 0; i < 16; i++)
        sprintf(&md5string[i*2], "%02x", (unsigned int)digest[i]);
    return string(md5string);
}
```

This solution first converts the input string into a c-string using the c_str() method of the string class. Then it calculates the md5 hash of the c-string using the MD5 function from the openssl library. The resulting hash is stored in the digest array. Finally, the hash is converted into a hexadecimal string and returned.