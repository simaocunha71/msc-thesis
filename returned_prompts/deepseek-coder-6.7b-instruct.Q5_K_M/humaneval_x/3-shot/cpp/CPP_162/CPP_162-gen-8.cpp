    if (text.empty())
        return NULL;

    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);

    char md5string[33];
    for(int i = 0; i < 16; i++)
        sprintf(&md5string[i*2], "%02x", result[i]);
    md5string[32] = '\0';

    return string(md5string);
}

