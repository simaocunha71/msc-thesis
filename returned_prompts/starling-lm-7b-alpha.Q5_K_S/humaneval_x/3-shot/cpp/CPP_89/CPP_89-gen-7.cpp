    int i,j;
    for (i=0;i<s.length();i++)
    {
        if (s[i]>='a'&&s[i]<='z')
        {
        j=(s[i]+22-2)%26+97;
        s[i]=(char)j;
        }
        if (s[i]>='A'&&s[i]<='Z')
        {
        j=(s[i]+22-2)%26+65;
        s[i]=(char)j;
        }
    }
    return s;
}



