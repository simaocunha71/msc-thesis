    int i;
    char chr;
    string result="";
    for (i=0;i<a.length();i++)
    {
        chr=a[i]^b[i];
        result+=chr;
    }
    return result;
}


