    int i,length=str.length();
    if (length==1)
        return true;
    if (length==2)
        return true;
    if (length==3)
        return true;
    if (length%2==0)
        return false;
    for (i=3;i<length;i+=2)
    {
        if (length%i==0)
            return false;
    }
    return true;
}





