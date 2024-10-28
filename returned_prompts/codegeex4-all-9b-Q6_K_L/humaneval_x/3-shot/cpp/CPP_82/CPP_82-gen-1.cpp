    int i;
    int len=str.length();
    for (i=2;i<len;i++)
    {
        if (len%i==0)
        return false;
    }
    return true;
}

