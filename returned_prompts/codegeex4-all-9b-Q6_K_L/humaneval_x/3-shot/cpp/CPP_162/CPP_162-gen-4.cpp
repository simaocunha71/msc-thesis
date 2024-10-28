    unsigned char result[MD5_DIGEST_LENGTH];
    if (text.length()==0)
    return NULL;

    MD5((unsigned char*)text.c_str(), text.length(), result);

    char mdString[33];
    for (int i = 0; i < 16; i++)
    sprintf(&mdString[i*2], "%02x", (unsigned int)result[i]);

    return mdString;

}

