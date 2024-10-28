    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);
    string md5_result;
    char md5_string[33];
    for (int i=0;i<33;i++)
    md5_string[i]=result[i];
    md5_result=md5_string;
    return md5_result;
}

