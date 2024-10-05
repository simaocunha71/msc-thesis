    string result;
    int i;
    for (i=0;i<a.length();i++)
    {
        if ((a[i]-'0')^((b[i]-'0'))==1)
        result+=('1');
        else
        result+=('0');
    }
    return result;
}