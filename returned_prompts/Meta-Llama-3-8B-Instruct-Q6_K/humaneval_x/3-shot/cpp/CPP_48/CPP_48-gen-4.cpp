    int i,j;
    j=text.length()-1;
    for (i=0;i<=j;i++)
    {
        if (text[i]!=text[j-i])
        return false;
    }
    return true;
}