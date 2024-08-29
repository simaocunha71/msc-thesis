```cpp
#include <openssl/md5.h>
#include <string>
#include <sstream>

string string_to_md5(const string& text) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.size(), (unsigned char*)&digest);

    stringstream ss;
    for(int i = 0; i < MD5_DIGEST_LENGTH; ++i)
        ss << hex << setw(2) << setfill('0') << (int)digest[i];
    return ss.str();
}
```
