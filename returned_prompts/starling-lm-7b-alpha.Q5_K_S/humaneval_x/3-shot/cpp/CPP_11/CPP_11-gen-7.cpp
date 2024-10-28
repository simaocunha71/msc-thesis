    int i;
    string result;
    for (i=0;i<a.length();i++)
    {
        if (a[i]=='0'&&b[i]=='0')
        result+='0';
        if (a[i]=='0'&&b[i]=='1')
        result+='1';
        if (a[i]=='1'&&b[i]=='0')
        result+='1';
        if (a[i]=='1'&&b[i]=='1')
        result+='0';
    }
    return result;
}

