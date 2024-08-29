```cpp
#include<iostream>
#include<openssl/md5.h>
#include<string>
using namespace std;
string string_to_md5(string text) {
    unsigned char c[MD5_DIGEST_LENGTH];
    char mdString[33];
    MD5((unsigned char*)text.c_str(), text.length(), c);
    for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
    {
        sprintf(&mdString[i*2], "%02x", (unsigned int)c[i]);
    }
    return mdString;
}
int main()
{
    cout<<string_to_md5("Hello world")<<endl;
    return 0;
}
```