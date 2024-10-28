    int sum=0;
    int i;
    for (i=0;i<lst.size();i+=2)
    if (lst[i]%2!=0)
    sum+=lst[i];
    return sum;
}


