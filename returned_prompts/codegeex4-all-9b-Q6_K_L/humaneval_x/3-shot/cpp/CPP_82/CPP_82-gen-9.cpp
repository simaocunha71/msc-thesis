    int i;
    int len=str.length();
    if (len==1||len==2)
    return true;
    for (i=2;i<len;i++)
    if (len%i==0)
    return false;
    return true;
}

