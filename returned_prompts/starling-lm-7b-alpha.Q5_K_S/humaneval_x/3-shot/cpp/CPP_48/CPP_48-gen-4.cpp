    int i,j;
    for (i=0;i<text.length();i++)
    {
        j=text.length()-i-1;
        if (text[i]!=text[j])
        return false;
    }
    return true;
}



