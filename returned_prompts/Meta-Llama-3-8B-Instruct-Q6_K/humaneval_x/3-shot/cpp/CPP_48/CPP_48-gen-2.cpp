    int i,j;
    i=0;
    j=text.length()-1;
    while (i<j)
    {
        if (text[i]!=text[j])
        return false;
        i++;
        j--;
    }
    return true;
}  // or return text==string(text.rbegin(),text.rend());  // this is more elegant but less efficient
}  // this one is more efficient but less elegant
