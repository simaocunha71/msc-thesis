    string result;
    int i;
    for (i=0;i<a.length();i++)
    {
        if (a[i]=='1' && b[i]=='1')
        result+='0';
        else if (a[i]=='0' && b[i]=='0')
        result+='0';
        else if (a[i]=='0' && b[i]=='1')
        result+='1';
        else if (a[i]=='1' && b[i]=='0')
        result+='1';
    }
    return result;
}


