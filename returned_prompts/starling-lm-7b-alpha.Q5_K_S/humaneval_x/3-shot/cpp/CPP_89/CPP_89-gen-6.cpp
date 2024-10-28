    string encrypted;
    int i,n;
    n=s.length();
    for (i=0;i<n;i++)
    {
        if (s[i]>='a' && s[i]<='z')
        encrypted+=char(s[i]+2);
        else if (s[i]>='A' && s[i]<='Z')
        encrypted+=char(s[i]+2);
        else
        encrypted+=s[i];
    }
    return encrypted;
}




