    int count=0;
    int i;
    for (i=11;i<n;i+=11)
    if (i%13==0)
    count+=1;
    for (i=13;i<n;i+=13)
    if (i%11==0)
    count+=1;
    return count;
}


