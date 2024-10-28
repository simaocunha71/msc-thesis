    int i;
    for  (i=0;i<s.length();i++)
    {
        if  (islower(s[i]))
        {
            s[i]=toupper(s[i]);
        }
        else if  (isupper(s[i]))
        {
            s[i]=tolower(s[i]);
        }
    }
    return s;
}


