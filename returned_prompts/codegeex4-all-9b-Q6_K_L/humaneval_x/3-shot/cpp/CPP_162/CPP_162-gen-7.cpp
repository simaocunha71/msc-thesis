    unsigned char digest[MD5_DIGEST_LENGTH];
    if (text.length()==0)
    return "None";
    MD5((unsigned char *)text.c_str(), text.length(), (unsigned char *)&digest);
    char mdString[MD5_DIGEST_LENGTH*2+1];
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
    sprintf(&mdString[i*2], "%02x", (unsigned int)digest[i]);
    return mdString;
}