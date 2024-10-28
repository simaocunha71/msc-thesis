    int i;
    int length=s.length();
    string result;
    for (i=0;i<length;i++)
    {
        if (s[i]>='a' && s[i]<='z')
        result+=char(s[i]-'a'+'A');
        else if (s[i]>='A' && s[i]<='Z')
        result+=char(s[i]-'A'+'a');
        else result+=s[i];
    }
    return result;
}



