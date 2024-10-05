    int res=0;
    for (int i=1;i<=n;i++)
    {
        int left=n-i;
        if (left==0) res+=1;
        else if (left>0) res+=10;
    }
    return res;
}


