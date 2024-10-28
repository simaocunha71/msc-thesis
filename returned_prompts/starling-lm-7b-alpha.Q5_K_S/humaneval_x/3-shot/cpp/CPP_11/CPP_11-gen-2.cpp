    int i;
    string result;
    for (i=0;i<a.length();i++)
    {
        if (a[i]==b[i])
        result+=a[i];
        else
        result+='1';
    }
    return result;
}


