    int i,j;
    for(i=0;i<text.length();i++)
    for(j=text.length()-1-i;j>=0;j--)
    if (text[i]!=text[j])
    return false;
    return true;
}

