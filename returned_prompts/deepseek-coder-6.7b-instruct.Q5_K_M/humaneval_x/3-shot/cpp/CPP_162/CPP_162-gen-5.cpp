    if (text.empty()) 
        return "";

    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);

    char md5_string[33] = {0};
    for(int i = 0; i < 16; ++i)
        sprintf(&md5_string[i*2], "%02x", result[i]);

    return string(md5_string);
}


