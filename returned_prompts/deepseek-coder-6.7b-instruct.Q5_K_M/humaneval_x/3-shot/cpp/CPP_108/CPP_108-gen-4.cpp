    int count=0;
    for (int i=0;i<n.size();i++)
    {
        int num=n[i];
        int sum=0;
        while(num)
        {
            sum+=num%10;
            num/=10;
        }
        if(sum>0) count++;
    }
    return count;
}

