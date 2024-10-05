    int i,count=0;
    for (i=0;i<n.size();i++)
    {
        int temp=abs(n[i]);
        int sum_digits=0;
        while (temp!=0)
        {
            sum_digits+=temp%10;
            temp=temp/10;
        }
        if (sum_digits>0)
        {
            count+=1;
        }
    }
    return count;
}




