    int sum=0;
    int i;
    for(i=0;i<k;i++)
    {
        if(log10(arr[i])+1<=2)
            sum+=arr[i];
    }
    return sum;
}