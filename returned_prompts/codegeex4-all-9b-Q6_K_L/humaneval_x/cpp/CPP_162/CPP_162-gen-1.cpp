#include <iostream>
#include <string>
#include <openssl/md5.h>
#include <sstream>
#include <iomanip>

std::string string_to_md5(std::string text) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char *)text.c_str(), text.size(), (unsigned char *)&digest);

    std::ostringstream ss;
    for(int i = 0; i < MD5_DIGEST_LENGTH; ++i)
        ss << std::hex << std::setw(2) << std::setfill('0') << (unsigned int)digest[i];
    return ss.str();
}

int main() {
    std::string text = "Hello world";
    std::string md5 = string_to_md5(text);
    std::cout << md5 << std::endl; // Should print "3e25960a79dbc69b674cd4ec67a72c62"
    return 0;
}

```cpp
#include <iostream>
#include <string>
#include <openssl/md5.h>
#include <sstream>
#include <iomanip>

std::string string_to_md5(std::string text) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char *)text.c_str(), text.size(), (unsigned char *)&digest);

    std::ostringstream ss;
    for(int i = 0; i < MD5_DIGEST_LENGTH; ++i)
        ss << std::hex << std::setw(2) << std::setfill('0') << (unsigned int)digest[i];
    return ss.str();
}

int main() {
    std::string text = "Hello world";
    std::string md5 = string_to_md5(text);
    std::cout << md5 << std::endl; // Should print "3e25960a79dbc69b674cd4ec67a72c62"
    return 0;
}
```
