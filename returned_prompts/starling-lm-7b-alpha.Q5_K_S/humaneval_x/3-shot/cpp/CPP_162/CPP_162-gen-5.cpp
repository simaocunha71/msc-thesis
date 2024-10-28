    if (text.size()==0) return "";
    unsigned char md5_result[16];
    MD5((const unsigned char*)text.c_str(),(int)text.size(),md5_result);
    string result;
    for (int i=0;i<16;i++)
    {
        char tmp[3];
        sprintf(tmp,"%02X",md5_result[i]);
        result+=tmp;
    }
    return result;
}



