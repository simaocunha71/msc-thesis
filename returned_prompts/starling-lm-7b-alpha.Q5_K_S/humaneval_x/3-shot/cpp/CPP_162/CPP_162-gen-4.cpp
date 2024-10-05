    if (text.length()==0) return "";
    unsigned char md5_hash[MD5_DIGEST_LENGTH];
    MD5((unsigned char *)text.c_str(), text.length(), md5_hash);
    string result;
    for (int i=0;i<MD5_DIGEST_LENGTH;i++)
    {
    result+=sprintf("%02x", md5_hash[i]);
    }

    return result;
}


