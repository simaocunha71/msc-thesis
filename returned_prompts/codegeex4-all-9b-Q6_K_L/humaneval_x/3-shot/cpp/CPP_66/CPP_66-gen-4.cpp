    int sum=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]>=65 && s[i]<=90)
        sum+=int(s[i]);
    }
    return sum;
}

