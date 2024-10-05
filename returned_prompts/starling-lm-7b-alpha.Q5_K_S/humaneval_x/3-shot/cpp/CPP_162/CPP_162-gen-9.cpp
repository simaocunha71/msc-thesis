    if (text.length()==0)
    return "";

    unsigned char md5result[16];
    MD5((unsigned char*)text.c_str(),(int)text.length(),md5result);
    string result;
    for (int i=0;i<16;i++)
    result+=sprintf("%02x",md5result[i]);
    return result;
}


