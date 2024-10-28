    int i,j;
    for (i=0;i<text.length();i++)
    for (j=text.length()-1;j>i;j--)
    if (text[i]!=text[j])
    return false;

    return true;
}



