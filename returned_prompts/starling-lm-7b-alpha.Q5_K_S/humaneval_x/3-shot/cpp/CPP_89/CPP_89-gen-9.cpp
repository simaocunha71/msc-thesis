    int i,j;
    char c;
    for (i=0;i<s.length();i++)
    {
        c=s[i];
        if ((c>='a')&&(c<='z'))
        {
        j=c-'a';
        j+=2*2;
        c=j+'a';
        }
        if ((c>='A')&&(c<='Z'))
        {
        j=c-'A';
        j+=2*2;
        c=j+'A';
        }
        s[i]=c;
    }
    return s;
}



