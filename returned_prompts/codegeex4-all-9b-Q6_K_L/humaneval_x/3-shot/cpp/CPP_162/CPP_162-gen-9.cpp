    unsigned char digest[MD5_DIGEST_LENGTH];
    char c[2];
    c[1]='\0';

    MD5_CTX context;
    MD5_Init(&context);
    for (int i=0;i<text.length();i++)
    {
        c[0]=text[i];
        MD5_Update(&context, c, 1);
    }
    MD5_Final(digest, &context);

    string out="";
    for (int i=0;i<MD5_DIGEST_LENGTH;i++)
        out=out+sprintf("%02x",digest[i]);

    return out;
}

