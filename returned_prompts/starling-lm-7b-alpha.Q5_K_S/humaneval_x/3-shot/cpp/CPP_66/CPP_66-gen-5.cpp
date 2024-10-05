    int i,sum=0,c;
    for (i=0;i<s.length();i++)
    {
        c=s[i];
        if (c>='A'&&c<='Z')
        sum+=c;
    }
    return sum;
}


