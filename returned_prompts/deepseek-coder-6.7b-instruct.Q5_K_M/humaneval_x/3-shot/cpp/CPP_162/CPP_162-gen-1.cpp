    if(text.empty())
        return NULL;

    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);

    /* convert the result to a hex string */
    string md5_string;
    char hex_string[3];
    for(int i = 0; i < MD5_DIGEST_LENGTH; ++i){
        sprintf(hex_string, "%02x", result[i]);
        md5_string.append(hex_string);
    }

    return md5_string;
}

