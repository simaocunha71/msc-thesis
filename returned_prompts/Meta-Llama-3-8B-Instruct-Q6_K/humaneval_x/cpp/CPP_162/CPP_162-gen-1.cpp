    if(text.empty()){
        return "";
    }
    unsigned char md5[MD5_DIGEST_LENGTH];
    string output;
    MD5(text.c_str(), text.size(), md5);
    for(int i = 0; i < MD5_DIGEST_LENGTH; i++){
        output += sprintf("%02x", md5[i]);
    }
    return output;
}
string string_to_md5(string text) {
    if (text.empty()) {
        return "";
    }
    unsigned char md5[MD5_DIGEST_LENGTH];
    string output;
    MD5((unsigned char*)text.c_str(), text.size(), md5);
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        output += sprintf("%02x", md5[i]);
    }
    return output;
}
