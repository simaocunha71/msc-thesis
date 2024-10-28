    int i;
    int length=text.length();
    for  (i=0;i<length/2;i++)
    {
        if  (text[i] != text[length-1-i])
        return false;
    }
    return true;
}


