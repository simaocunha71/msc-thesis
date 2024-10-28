    int len=str.length();
    int i;
    for (i=2;i<=sqrt(len);i++)
    if (len%i==0)
    return false;
    return true;
}


