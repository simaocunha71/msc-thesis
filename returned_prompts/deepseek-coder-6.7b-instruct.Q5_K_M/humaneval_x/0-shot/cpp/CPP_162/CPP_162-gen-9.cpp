if(text.empty())
{
return NULL;
}

B:
unsigned char result[MD5_DIGEST_LENGTH];
MD5((unsigned char*)text.c_str(), text.size(), result);

C:
char md5string[33];
for(int i=0; i<16; i++){
sprintf(&md5string[i*2], "%02x", (unsigned int)result[i]);
}
return string(md5string);
}

The code uses the OpenSSL library to compute the MD5 hash of the input string.
If the string is empty, it returns NULL.
The MD5 hash is computed and stored in 'result'. 
Then the hash is converted to a hexadecimal string and returned.
*/

int main(){
string text = "Hello world";
string md5_hash = string_to_md5(text);
cout << "MD5 hash of '" << text << "' is: "<< md5_hash << endl;
return 0;
}


A: Here is the C++ code that does what you want:

```cpp
#include <iostream>
#include <string>
#include <openssl/md5.h>

using namespace std;

string string_to_md5(string text){
    if(text.empty())
        return NULL;
    
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.size(), result);

    char md5string[33];
    for(int i=0; i<16; i++)
        sprintf(&md5string[i*2], "%02x", (unsigned int)result[i]);
    
    return string(md5string);
}

int main(){
    string text = "Hello world";
    string md5_hash = string_to_md5(text);
    cout << "MD5 hash of '" << text << "' is: "<< md5_hash << endl;
    return 0;
}
```

This code uses OpenSSL library to compute MD5 hash of a