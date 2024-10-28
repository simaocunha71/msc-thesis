    if (text=="")
    return "";
    unsigned char hash[MD5_DIGEST_LENGTH];
    MD5_CTX md5;
    MD5_Init(&md5);
    MD5_Update(&md5, text.c_str(), text.length());
    MD5_Final(hash, &md5);
    stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
    ss << hex << setw(2) << setfill('0') << (int)hash[i];
    return ss.str();
}



