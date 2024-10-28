    int sum=0;
    int i;
    for (i=0;i<k;i++)
    {
        int temp=arr[i];
        if (temp<10)
        sum+=temp;
        if (temp>=10 && temp<100)
        sum+=temp;
    }
    return sum;
}

