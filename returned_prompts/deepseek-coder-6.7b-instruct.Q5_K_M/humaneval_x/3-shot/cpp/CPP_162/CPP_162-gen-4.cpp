    if (text.empty()) {
        return "";
    }
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);
    char buffer[33];
    for(int i = 0; i < 16; ++i)
        sprintf(&buffer[i*2], "%02x", result[i]);
    return string(buffer);
}



