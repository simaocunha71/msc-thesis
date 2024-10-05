    if (text.empty()) 
        return "";
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);
    return string((char*)result, MD5_DIGEST_LENGTH);
}

