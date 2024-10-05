    int i,len;
    char chr;
    len=a.length();
    string result="";
    for (i=0;i<len;i++)
    {
        chr=a[i]^b[i];
        result+=chr;
    }
    return result;
}


