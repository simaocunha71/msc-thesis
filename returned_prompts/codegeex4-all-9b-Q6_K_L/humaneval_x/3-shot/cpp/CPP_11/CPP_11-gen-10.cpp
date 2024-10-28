    string result;
    int i;
    int x;
    for (i=0;i<a.length();i++)
    {
        x=a[i]^b[i];
        result+=x;
    }
    return result;
}

