```cpp
#include <cstdio>
#include <string>
#include <openssl/md5.h>
using namespace std;

string string_to_md5(string text){
    unsigned char c[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), c);
    char mdString[MD5_DIGEST_LENGTH*2+1];
    for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
        sprintf(&mdString[i*2], "%02x", (unsigned int)c[i]);
    return string(mdString);
}
```