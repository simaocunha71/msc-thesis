    int i;
    string res="";
    for (i=0;i<s.length();i++)
    {
        if (s[i]>='a'&&s[i]<='z')
        res+=(char)(s[i]-32);
        else
        if (s[i]>='A'&&s[i]<='Z')
        res+=(char)(s[i]+32);
        else
        res+=s[i];
    }
    return res;
}



