```cpp
#include <sstream>
#include <iomanip>
#include <openssl/md5.h>
#include <string>
#include <sstream>
#include <iomanip>

std::string string_to_md5(std::string text) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), (unsigned char*)&digest);

    std::stringstream ss;
    for(int i = 0; i < MD5_DIGEST_LENGTH; ++i)
    {
        ss << std::hex << std::setw(2) << std::setfill('0') << (unsigned int)digest[i];
    }

    return ss.str();
}
```