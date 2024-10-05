    int sum=0;
    int i;
    for (i=0;i<k;i++)
    {
        int temp=arr[i];
        int j;
        int count=0;
        while (temp!=0)
        {
            count+=1;
            temp=temp/10;
        }
        if (count<=2)
        sum+=arr[i];
    }
    return sum;
}

