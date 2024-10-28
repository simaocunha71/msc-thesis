    int i,sum=0;
    for (i=0;i<lst.size();i++)
    if ((i%2==0)&&(lst[i]%2==1)) sum+=lst[i];
    return sum;
}



