    int count=0;
    int num;
    int digit;
    for  (int i=0;i<n.size();i++)
    {
        num=abs(n[i]);
        digit=0;
        while  (num>0)
        {
            digit+=num%10;
            num/=10;
        }
        if  (digit>0)
        count++;
    }
    return count;
}


