    MD4_Init(&c);
    MD4_Update(&c, (unsigned char *)&nonce, sizeof(nonce));
    MD4_Final((unsigned char *)hash, &c);
#endif
