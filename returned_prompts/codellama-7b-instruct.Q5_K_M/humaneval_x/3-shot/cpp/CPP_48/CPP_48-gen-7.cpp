    int i,j,len;
    len=text.length();
    for (i=0,j=len-1;i<len;i++,j--)
    if (text[i]!=text[j])
    return false;
    return true;
}


