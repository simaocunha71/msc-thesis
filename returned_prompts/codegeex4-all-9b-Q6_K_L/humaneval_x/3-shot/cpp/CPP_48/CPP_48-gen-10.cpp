    int i=0;
    int j=text.length()-1;
    while (i<j)
    {
        if (text[i]!=text[j])
        return false;
        i+=1;
        j-=1;
    }
    return true;
}

