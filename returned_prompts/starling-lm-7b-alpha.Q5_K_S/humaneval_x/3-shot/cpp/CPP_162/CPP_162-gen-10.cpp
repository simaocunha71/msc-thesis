    if (text.size()==0) return "";
    unsigned char digest[16];
    MD5((const unsigned char*)text.c_str(),(int)text.size(),digest);
    string result;
    for (int i=0;i<16;i++)
    {
        char buffer[3];
        sprintf(buffer,"%02x",digest[i]);
        result+=buffer;
    }
    return result;
}




