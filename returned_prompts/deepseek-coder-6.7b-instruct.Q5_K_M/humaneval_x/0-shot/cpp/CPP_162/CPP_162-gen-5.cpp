if (text == ""){
        return NULL;
    }
B:
unsigned char result[MD5_DIGEST_LENGTH];
MD5((unsigned char*)text.c_str(), text.length(), result);
C:
char md5string[33];
for(int i = 0; i < 16; i++){
        sprintf(&md5string[i*2], "%02x", (unsigned int)result[i]);
    }
return string(md5string);
}


A: You can use the OpenSSL library to compute the MD5 hash of a string.
Here is the C++ code for your question:

```cpp
#include <openssl/md5.h>
#include <string>
#include <iomanip>
#include <sstream>

std::string string_to_md5(const std::string& text)
{
    if (text.empty())
        return "";

    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);

    std::stringstream ss;
    for(int i = 0; i < MD5_DIGEST_LENGTH; ++i)
    {
        ss << std::hex << std::setw(2) << std::setfill('0') << (unsigned int)result[i];
    }

    return ss.str();
}
```

This code will return an empty string if the input is an empty string, otherwise it will return the MD5 hash of the input string.

Note: Make sure to link against the OpenSSL library and include the OpenSSL header files.

```cpp
#include <openssl/applink.c>
```

This is the OpenSSL version of the MD5 function. If you are using a different version of OpenSSL, you may need to adjust the function name.

Remember to use the OpenSSL library and its header files in your program to compile this code.

Also, the OpenSSL library is not included in the standard C++ library, you have to install it separately.

In Ubuntu, you can install it by using the following command:

```bash