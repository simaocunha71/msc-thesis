    int i,j,k;
    for (i=0,j=text.length()-1,k=0;k<text.length();i++,j--,k++)
    if (text[i]!=text[j])
    return false;

    return true;
}


