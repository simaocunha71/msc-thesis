    int i,length;
    length=str.length();
    for (i=2;i<=sqrt(length);i++)
    if (length%i==0)
    return false;

    return true;
}



