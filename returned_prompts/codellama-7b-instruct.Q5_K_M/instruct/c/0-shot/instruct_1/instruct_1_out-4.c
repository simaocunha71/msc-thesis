
    unsigned char *md5(unsigned char *input)
    {
        return MD5((unsigned char *)input, strlen((char *)input), NULL);
    }

