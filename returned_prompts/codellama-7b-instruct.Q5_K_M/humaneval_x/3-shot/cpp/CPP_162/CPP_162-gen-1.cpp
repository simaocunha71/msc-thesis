    unsigned char hash[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), hash);
    string hash_str = "";
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        stringstream ss;
        ss << setfill('0') << setw(2) << hex << (int)hash[i];
        hash_str += ss.str();
    }
    return hash_str;
}


