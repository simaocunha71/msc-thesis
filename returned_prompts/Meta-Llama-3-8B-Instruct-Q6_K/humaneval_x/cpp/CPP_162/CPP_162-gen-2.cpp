if(text.empty()) return ""; // return empty string if input is empty
char output[33]; // buffer to store the hash
MD5_CTX md5; // create a new MD5 context
MD5_Init(&md5); // initialize the MD5 context
MD5_Update(&md5, text.c_str(), text.length()); // update the hash with the input text
MD5_Final(output, &md5); // finalize the hash
return string(output, 32); // convert the hash to a string and return it
}

B:
#include <string>
#include <iostream>
#include <md5.h>

std::string string_to_md5(const std::string& text) {
    if (text.empty()) return ""; // return empty string if input is empty

    std::string output;
    unsigned char hash[16];

    MD5_CTX md5;
    MD5_Init(&md5);
    MD5_Update(&md5, text.c_str(), text.length());
    MD5_Final(hash, &md5);

    for (int i = 0; i < 16; ++i) {
        output += std::hex;
        output += static_cast<char>(hash[i]);
    }

    return output;
}

int main() {
    std::cout << string_to_md5("Hello world") << std::endl;
    return 0;
}

C:
#include <iostream>
#include <string>
#include <openssl/md5.h>

std::string string_to_md5(const std::string& text) {
    if (text.empty()) return ""; // return empty string if input is empty

    unsigned char hash[16];
    MD5((unsigned char*)text.c_str(), text.length(), hash);

    std::string output;
    for (int i = 0; i < 16; ++i) {
        output += std::hex;
        output += static_cast<char>(hash[i]);
    }

    return output;
}

int main() {
    std::cout << string_to_md5("Hello world") << std::endl;
    return 0;
}

D:
#include <iostream>
#include <string>
#include <algorithm>
#include <openssl/evp.h>

std::string string_to_md5(const std::string& text) {
    if (text.empty()) return ""; // return empty string if input is empty

    unsigned char hash[16];
    EVP_MD_CTX mdctx;
    EVP_MD_CTX_init(&mdctx);
    EVP_DigestInit