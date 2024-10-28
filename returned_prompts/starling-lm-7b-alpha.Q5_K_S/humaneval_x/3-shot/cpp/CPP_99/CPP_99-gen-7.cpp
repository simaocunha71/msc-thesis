    int i,j,n;
    int res=-1;
    int d=abs(res-value[0]-'0');
    for (i=0;i<value.size();i++)
    {
        j=value[i]-'0';
        n=j*pow(10,value.size()-i-1);
        if (abs(n-res)>d)
        {
            res=n;
            d=abs(n-res);
        }
    }
    return res;
}


