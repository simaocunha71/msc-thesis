    int i,sum=0;
    for (i=0;i<lst.size();i++)
    if (lst[i]%2==0 && i%2==1)
    sum+=lst[i];

    return sum;
}


