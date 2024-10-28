    if (n<0)
    {
        printf("Invalid input. n must be a positive integer.\n");
        return -1;
    }
    if (n==0)
    {
        return 0;
    }
    if (n==1)
    {
        return 0;
    }
    if (n==2)
    {
        return 2;
    }
    if (n==3)
    {
        return 0;
    }
    int fib4_0=0,fib4_1=0,fib4_2=2,fib4_3=0;
    for (int i=4;i<=n;i++)
    {
        int temp=fib4_0+fib4_1+fib4_2+fib4_3;
        fib4_3=fib4_2;
        fib4_2=fib4_1;
        fib4_1=fib4_0;
        fib4_0=temp;
    }
    return fib4_0;
}  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might need to be revised.  // This function is not tested yet. It might