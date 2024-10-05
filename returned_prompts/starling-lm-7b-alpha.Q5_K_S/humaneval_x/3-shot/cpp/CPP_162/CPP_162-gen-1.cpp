    MD5_CTX context;
    MD5_Init(&context);
    MD5_Update(&context, text.c_str(), text.length());
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5_Final(digest, &context);
    char result[MD5_DIGEST_LENGTH*2+1];
    sprintf(result, "%0x", (unsigned int) *(int *)digest);
    return result;
}



