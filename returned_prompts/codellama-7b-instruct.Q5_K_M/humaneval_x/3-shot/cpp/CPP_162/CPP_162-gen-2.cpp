    if (text=="")
    return "None";
    else
    {
        unsigned char digest[MD5_DIGEST_LENGTH];
        MD5((unsigned char*)text.c_str(), text.length(), (unsigned char*)&digest);
        stringstream ss;
        for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
        ss << hex << setw(2) << setfill('0') << (int)digest[i];
        return ss.str();
    }
}


