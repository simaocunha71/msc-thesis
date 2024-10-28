    string c;
    int i,n=a.length();
    for (i=0;i<n;i++)
    {
        if (a[i]=='0' && b[i]=='0') c+='0';
        if (a[i]=='0' && b[i]=='1') c+='1';
        if (a[i]=='1' && b[i]=='0') c+='1';
        if (a[i]=='1' && b[i]=='1') c+='0';
    }
    return c;
}



