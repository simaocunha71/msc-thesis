    int count=0;
    int temp;
    int digit;
    int i;
    int j;
    for  (i=0;i<n.size();i++)
    {
        temp=abs(n[i]);
        digit=0;
        while  (temp>0)
        {
            digit+=temp%10;
            temp/=10;
        }
        if  (n[i]<0)
        digit*=-1;
        if  (digit>0)
        count+=1;
    }
    return count;
}



