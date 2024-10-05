    int sum=0;
    int i;
    for  (i=0;i<k;i++)
    {
        if  ((arr[i]>=10 && arr[i]<=99)||(arr[i]>=-99 && arr[i]<=-10))
        sum+=arr[i];
    }
    return sum;
}


