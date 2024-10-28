    if (text=="" && text.length()==0)
    return "None";

    else{
    unsigned char md5_hash[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), md5_hash);
    stringstream ss;
    for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
    ss << hex << setw(2) << setfill('0') << (int)md5_hash[i];
    return ss.str();
    }
}


