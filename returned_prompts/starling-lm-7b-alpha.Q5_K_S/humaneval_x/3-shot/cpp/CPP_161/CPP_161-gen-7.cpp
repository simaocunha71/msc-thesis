    int i;
    int length = s.length();
    for (i=0;i<length;i++)
    {
        if (s[i]>='a'&&s[i]<='z')
        {
            s[i]=s[i]-32;
        }
        else if (s[i]>='A'&&s[i]<='Z')
        {
            s[i]=s[i]+32;
        }
    }
    return s;
}







