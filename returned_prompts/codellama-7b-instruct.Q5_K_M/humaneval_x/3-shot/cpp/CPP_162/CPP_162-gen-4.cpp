    if (text=="") return "";
    unsigned char hash[MD5_DIGEST_LENGTH];
    MD5((const unsigned char*)text.c_str(), text.length(), hash);
    stringstream ss;
    for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
        ss << hex << setw(2) << setfill('0') << (int)hash[i];
    return ss.str();
}

