    if (text.length()==0)
    return "";
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((const unsigned char*)text.c_str(),(int)text.length(),result);
    string md5_string;
    int i;
    for (i=0;i<MD5_DIGEST_LENGTH;i++)
    md5_string+=result[i];
    return md5_string;
}


