    int count=0;
    for (int i=0;i<n.size();i++)
    {
        int sum=0;
        int abs_num = abs(n[i]);
        while (abs_num>0)
        {
            sum+=abs_num%10;
            abs_num/=10;
        }
        if (sum>0)
            count++;
    }
    return count;
}

