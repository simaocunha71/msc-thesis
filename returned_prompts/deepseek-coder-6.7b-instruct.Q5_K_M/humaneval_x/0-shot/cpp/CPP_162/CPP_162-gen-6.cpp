    if (text.length()==0) return NULL;
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);
    char md5string[33];
    for(int i=0; i < 16; ++i) sprintf(&md5string[i*2], "%02x", result[i]);
    return string(md5string);
}
int main() {
    printf("%s\n", string_to_md5("Hello world").c_str());
}

*/

A: You had some syntax error in your code. Here's the corrected version:

```cpp
#include<iostream>
#include<string>
#include<openssl/md5.h>
using namespace std;

string string_to_md5(string text){
    if (text.length()==0) return NULL;
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);
    char md5string[33];
    for(int i=0; i < 16; ++i) sprintf(&md5string[i*2], "%02x", result[i]);
    return string(md5string);
}

int main() {
    printf("%s\n", string_to_md5("Hello world").c_str());
}
```

Please note that the MD5 function is considered insecure and unsafe for further