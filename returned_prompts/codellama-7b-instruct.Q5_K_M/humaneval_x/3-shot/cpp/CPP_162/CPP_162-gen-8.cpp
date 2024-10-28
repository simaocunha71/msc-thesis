    if (text=="")
    return "";
    else{
    unsigned char hash[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(),text.length(),hash);
    string hash_string;
    for (int i=0;i<MD5_DIGEST_LENGTH;i++)
    {
        stringstream ss;
        ss << std::hex << (int)hash[i];
        hash_string+=ss.str();
    }
    return hash_string;
    }
}


