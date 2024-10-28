    int i;
    int last_three=0;
    int last_two=0;
    int last_one=0;
    int current=0;
    if (n==0)
    return 0;
    if (n==1)
    return 0;
    if (n==2)
    return 2;
    if (n==3)
    return 0;

    for (i=4;i<=n;i++)
    {
        current=last_three+last_two+last_one;
        last_three=last_two;
        last_two=last_one;
        last_one=current;
    }
    return current;
}


