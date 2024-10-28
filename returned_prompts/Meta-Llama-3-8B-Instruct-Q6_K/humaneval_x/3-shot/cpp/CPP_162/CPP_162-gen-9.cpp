    if(text.empty())
        return "";

    unsigned char md5[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.size(), md5);

    string result;
    for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
        sprintf("%02x", md5[i]), result += 0;

    return result;
}
// Note: You need to link your program with libcrypto, which is a part of OpenSSL library.
// You can do this by compiling your program with "-lcrypto" flag, for example:
// g++ -o your_program your_program.cpp -lcrypto
// On some platforms, you may need to use "-lssl" instead of "-lcrypto". 
// This is because OpenSSL's MD5 function is part of SSL library.