    if (text.length()==0) return "";
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(),text.size(),result);
    string hex_result;
    for (int i=0;i<MD5_DIGEST_LENGTH;i++)
    {
    sprintf(hex_result+"%02x",result[i]);
    }
    return hex_result;
}


