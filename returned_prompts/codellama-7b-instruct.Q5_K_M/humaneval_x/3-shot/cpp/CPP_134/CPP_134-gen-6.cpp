    int len=txt.length()-1;
    int i;
    for (i=0;i<len;i++)
    if (txt[i]==' '||txt[i]=='\t')
    len=i-1;
    if (txt[len]>='a'&&txt[len]<='z')
    return true;
    else
    return false;
}


