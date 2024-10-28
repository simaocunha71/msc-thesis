    int i,j;
    for  (i=0,j=text.size()-1;i<j;i++,j--)
    {
        if  (text[i] != text[j])
        return false;
    }
    return true;
}


