    int count=0;
    int i;
    int sum;
    for  (i=0;i<n.size();i++)
    {
        sum=0;
        int num=n[i];
        while  (num)
        {
            sum+=num%10;
            num/=10;
        }
        if  (sum>0)
        count++;
    }
    return count;
}


