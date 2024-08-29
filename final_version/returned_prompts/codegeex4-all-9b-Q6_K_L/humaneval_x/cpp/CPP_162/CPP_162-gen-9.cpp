```cpp
#include <openssl/md5.h>
#include <string>
#include <sstream>
#include <iomanip>
#include <iostream>

std::string string_to_md5(const std::string& text) {
    if (text.empty()) {
        return {};
    }

    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.size(), digest);

    std::stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; ++i) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (unsigned int)digest[i];
    }

    return ss.str();
}

int main() {
    std::string input = "Hello world";
    std::string md5hash = string_to_md5(input);
    std::cout << "MD5 hash of \"" << input << "\": " << md5hash << std::endl;
    return 0;
}
```

This solution uses OpenSSL's `MD5` function to calculate the MD5 hash of the input string. It then converts the resulting byte array into a hexadecimal string representation. The function checks if the input string is empty and returns an empty string if it is. The `main` function demonstrates how to use the `string_to_md5` function.