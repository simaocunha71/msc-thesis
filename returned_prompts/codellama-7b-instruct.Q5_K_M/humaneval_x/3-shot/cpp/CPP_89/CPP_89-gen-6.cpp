    int i;
    string encrypt_string;
    for (i=0;i<s.length();i++)
    {
        if (s[i]>='a'&&s[i]<='z')
        encrypt_string+=char(int(s[i])+2*2);
        if (s[i]>='A'&&s[i]<='Z')
        encrypt_string+=char(int(s[i])+2*2);
    }
    return encrypt_string;
}


