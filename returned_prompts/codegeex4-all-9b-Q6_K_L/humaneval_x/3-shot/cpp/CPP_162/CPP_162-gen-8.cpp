    unsigned char result[MD5_DIGEST_LENGTH];
    char *cstr = &text[0u];
    MD5((unsigned char*)cstr, strlen(cstr), result);
    char mdString[33];
    for(int i = 0; i < 16; i++)
    sprintf(&mdString[i*2], "%02x", (unsigned int)result[i]);
    return mdString;
}


