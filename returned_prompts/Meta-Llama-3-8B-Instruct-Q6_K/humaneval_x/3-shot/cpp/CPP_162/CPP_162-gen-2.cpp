    if(text.empty())
    return "";
    unsigned char md5[16];
    MD5((unsigned char*)text.c_str(), text.size(), md5);
    string result;
    for(int i=0; i<16; i++)
    {
        sprintf("%02x", md5[i]);
        result+=string(1, md5[i]);
    }
    return result;
} 
#endif // STRING_TO_MD5_H
#endif // STRING_TO_MD5_C


