    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, (unsigned char*)text.c_str(), text.size());
    unsigned char md5[16];
    MD5_Final(md5, &ctx);
    string result;
    for (int i=0;i<16;i++)
    {
        char buffer[3];
        sprintf(buffer,"%02x",md5[i]);
        result+=buffer;
    }
    return result;
}


