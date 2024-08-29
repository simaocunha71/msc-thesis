```cpp
#include <iostream>
#include <string>
#include <openssl/md5.h>

std::string string_to_md5(const std::string& text) {
    if (text.empty()) return "";

    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.size(), (unsigned char*)&digest);

    std::string md5_hash;
    char hex[3];
    for (int i = 0; i < MD5_DIGEST_LENGTH; ++i) {
        sprintf(hex, "%02x", digest[i]);
        md5_hash += hex;
    }

    return md5_hash;
}

int main() {
    std::cout << string_to_md5("Hello world") << std::endl;
    return 0;
}
```