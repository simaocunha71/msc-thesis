    if (n>m) return "-1";
    int total=(n+m);
    int average=total/(n-m+1);
    string result=to_string(average);
    int i,size;
    size=result.length();
    for (i=size-1;i>=0;i--)
    {
        if (result[i]=='0') result[i]='1';
        else {result[i]='0';break;}
    }
    return result;
}


