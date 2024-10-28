    int i,sum,count=0;
    for (i=0;i<n.size();i++)
    {
        sum=0;
        int number=n[i];
        while (number!=0)
        {
            sum+=number%10;
            number/=10;
        }
        if (sum>0)
        count++;
    }
    return count;
}



