    int i;
    int length = txt.length();
    for (i=length-1;i>=0;i--)
    if (txt[i]==' '||txt[i]=='\0')
    if (txt[i-1]>='a'&&txt[i-1]<='z'||txt[i-1]>='A'&&txt[i-1]<='Z')
    return true;
    return false;
}



