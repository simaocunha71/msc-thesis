    unsigned char c[MD5_DIGEST_LENGTH];
    char result[33];
    if (text=="")
    return NULL;
    MD5((unsigned char*)text.c_str(),text.length(),c);
    for (int i=0;i<32;i++)
    sprintf(&result[i*2],"%02x",c[i]);
    return result;
}

