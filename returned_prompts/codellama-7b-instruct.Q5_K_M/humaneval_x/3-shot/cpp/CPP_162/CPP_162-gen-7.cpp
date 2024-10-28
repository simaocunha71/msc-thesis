    if (text.length()==0)
    return "";
    else
    {
        MD5_CTX c;
        unsigned char hash[16];
        MD5_Init(&c);
        MD5_Update(&c, text.c_str(), text.length());
        MD5_Final(hash, &c);
        char *hex_string = new char[33];
        for (int i = 0; i < 16; i++) {
            sprintf(&hex_string[i * 2], "%02x", hash[i]);
        }
        return hex_string;
    }
}


