    int i,len;
    int shift=2*2;
    string encrypted_string;
    len=s.length();
    for (i=0;i<len;i++)
    {
        if (s[i]>='a' && s[i]<='z')
        encrypted_string+=char(int(s[i]+shift)%26+97);
        else
        encrypted_string+=s[i];
    }
    return encrypted_string;
}




