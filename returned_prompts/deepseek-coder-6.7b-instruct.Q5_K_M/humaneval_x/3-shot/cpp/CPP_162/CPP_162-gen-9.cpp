    if (text.empty())
    {
        return "";
    }
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);
    char output[MD5_DIGEST_LENGTH*2+1];
    for(int i=0; i<MD5_DIGEST_LENGTH; ++i)
    {
        sprintf(output + i*2, "%02x", result[i]);
    }
    return string(output);
}

