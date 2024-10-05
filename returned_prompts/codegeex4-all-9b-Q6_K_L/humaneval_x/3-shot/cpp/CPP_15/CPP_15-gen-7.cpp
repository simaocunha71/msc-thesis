    string str;
    int i;
    for (i=0;i<=n;i++)
    {
        str+=to_string(i);
        if (i<n)
        str+=" ";
    }
    return str;
}

