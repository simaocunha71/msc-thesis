    string s = to_string(n);
    int ret = 1;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]-'0'%2==1)
        ret*=s[i]-'0';
    }
    return ret;
}


