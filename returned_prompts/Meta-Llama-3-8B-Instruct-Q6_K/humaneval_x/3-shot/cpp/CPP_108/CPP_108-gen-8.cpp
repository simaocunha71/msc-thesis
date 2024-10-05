    int count=0;
    for (int i=0;i<n.size();i++)
    {
        if (n[i]>0)
        {
            int sum=0;
            int num=n[i];
            while(num>0)
            {
                sum+=num%10;
                num=num/10;
            }
            if (sum>0)
                count++;
        }
        else if (n[i]<0)
        {
            num=n[i];
            sum=1;
            while(num<0)
            {
                sum+=num%10;
                num=num/10;
            }
            if (sum>0)
                count++;
        }
    }
    return count;
}
```


