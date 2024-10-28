    int result=0;
    int i;
    int upper_bound=pow(10,n)-1;
    int lower_bound=pow(10,n-1);
    for (i=lower_bound;i<upper_bound;i++)
    if (i%10==1 || i/10==1)
    result+=1;

    return result;
}

