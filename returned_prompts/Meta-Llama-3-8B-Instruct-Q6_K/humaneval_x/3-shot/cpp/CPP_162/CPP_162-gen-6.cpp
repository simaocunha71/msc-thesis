    if (text.empty())
    return "";
    unsigned char md5[16];
    MD5((unsigned char*)text.c_str(), text.size(), md5);
    string result;
    for (int i = 0; i < 16; i++)
    {
        char c[3];
        sprintf(c, "%02x", md5[i]);
        result += c;
    }
    return result;
} // md5 hash string
// 3e25960a79dbc69b674cd4ec67a72c62


