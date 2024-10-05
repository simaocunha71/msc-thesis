    string encrypted;
    int i;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        encrypted+=chr+4;
    }
    return encrypted;
}

