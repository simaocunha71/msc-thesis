    if (text.empty()) return "";
    MD5_CTX md5;
    char md5_str[33];
    MD5_Init(&md5);
    MD5_Update(&md5, text.c_str(), text.size());
    MD5_Final((unsigned char *)md5_str, &md5);
    return md5_str;
}

