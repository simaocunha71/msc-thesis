    if (text.length()==0) return "";
    unsigned char result[16];
    MD5_CTX md5;
    MD5_Init(&md5);
    MD5_Update(&md5,text.c_str(),text.length());
    MD5_Final(result,&md5);
    string ret;
    for (int i=0;i<16;i++)
    ret+=sprintf("%02x",result[i]);
    return ret;
}


