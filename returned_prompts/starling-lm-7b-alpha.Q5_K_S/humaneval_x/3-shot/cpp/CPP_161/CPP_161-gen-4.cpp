    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]>='a' && s[i]<='z')
        {
        s[i]=s[i]-'a'+'A';
        }
        else if (s[i]>='A' && s[i]<='Z')
        {
        s[i]=s[i]-'A'+'a';
        }
    }
    return s.substr(s.length()-1,s.length())+s.substr(0,s.length()-1);
}



