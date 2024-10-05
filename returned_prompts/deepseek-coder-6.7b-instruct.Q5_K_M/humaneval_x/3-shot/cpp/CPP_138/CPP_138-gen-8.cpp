    int count=0;
    for(int i=2;i<n;i+=2)
    {
        if(n-i>=0)
        {
            n-=i;
            count+=1;
            i-=2;
        }
    }
    return n==0 && count==4;
}

