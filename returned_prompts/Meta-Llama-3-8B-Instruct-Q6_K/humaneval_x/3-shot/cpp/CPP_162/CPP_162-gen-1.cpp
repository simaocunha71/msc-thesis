    if(text.empty())
        return "";
    unsigned char md5[MD5_DIGEST_LENGTH];
    MD5((const unsigned char*)text.c_str(),text.length(),md5);
    string result;
    for(int i=0; i<MD5_DIGEST_LENGTH; i++)
        sprintf(result + strlen(result), "%02x", md5[i]);
    return result;
}
