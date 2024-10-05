    int i;
    int sum=0;
    for (i=0;i<lst.size();i++)
    if (i%3==0)
    sum+=pow(lst[i],2);
    else if (i%4==0)
    sum+=pow(lst[i],3);
    return sum;
}


