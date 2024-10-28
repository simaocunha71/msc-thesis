    int i;
    int count=0;
    for (i=2;i<=sqrt(a);i++)
    if (a%i==0)
    count+=1;
    if (count==0)
    return true;
    else
    return false;
}

