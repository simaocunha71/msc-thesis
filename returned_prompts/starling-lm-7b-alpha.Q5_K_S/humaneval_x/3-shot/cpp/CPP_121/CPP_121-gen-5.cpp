    int i, sum=0, length=lst.size();
    for (i=0;i<length;i++)
    if (lst[i]%2==1 && i%2==0)
    sum+=lst[i];

    return sum;
}




