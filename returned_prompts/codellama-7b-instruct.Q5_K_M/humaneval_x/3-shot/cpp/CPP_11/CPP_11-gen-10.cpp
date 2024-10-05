    string result="";
    int i;
    int len=a.length();
    for (i=0;i<len;i++)
    {
        if (a[i]==b[i])
        result+="0";
        else
        result+="1";
    }
    return result;
}




