    if (text=="")
    return "None";
    MD5_CTX c;
    unsigned char hash[16];
    MD5_Init(&c);
    MD5_Update(&c, text.c_str(), text.length());
    MD5_Final(hash, &c);
    stringstream ss;
    for(int i = 0; i < 16; i++)
    {
        ss << hex << setw(2) << setfill('0') << (int)hash[i];
    }
    return ss.str();
}


