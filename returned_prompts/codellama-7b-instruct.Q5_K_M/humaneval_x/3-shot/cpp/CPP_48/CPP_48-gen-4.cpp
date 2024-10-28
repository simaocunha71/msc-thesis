    int i,j;
    int len=text.length();
    for (i=0,j=len-1;i<len/2;i++,j--)
    if (text[i]!=text[j])
    return false;
    return true;
}


