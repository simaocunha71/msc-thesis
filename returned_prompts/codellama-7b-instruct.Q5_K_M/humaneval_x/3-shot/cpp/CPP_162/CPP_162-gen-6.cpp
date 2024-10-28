    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5_CTX c;
    MD5_Init(&c);
    MD5_Update(&c, text.c_str(), text.length());
    MD5_Final(digest, &c);
    stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        ss << hex << setfill('0') << setw(2) << (int)digest[i];
    }
    return ss.str();
}



