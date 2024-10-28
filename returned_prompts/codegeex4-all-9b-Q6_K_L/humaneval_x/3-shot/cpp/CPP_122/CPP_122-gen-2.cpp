    int sum=0;
    int i;
    for (i=0;i<k;i++)
    {
        if (arr[i]>=10)
        {
            sum+=arr[i]/10;
            sum+=arr[i]%10;
        }
        else
        sum+=arr[i];
    }
    return sum;
}

