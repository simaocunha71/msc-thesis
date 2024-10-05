    if (text.empty())
        return NULL;

    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), result);

    /* Convert the result to a hex string */
    string md5_string;
    char buffer[3]; 
    for(int i=0; i < MD5_DIGEST_LENGTH; i++){
        sprintf(buffer, "%02x", result[i]);
        md5_string.append(buffer);
    }
    return md5_string;
}


