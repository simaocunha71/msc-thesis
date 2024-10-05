    int sum=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (isupper(s[i]))
        sum+=s[i];
    }
    return sum;
}


