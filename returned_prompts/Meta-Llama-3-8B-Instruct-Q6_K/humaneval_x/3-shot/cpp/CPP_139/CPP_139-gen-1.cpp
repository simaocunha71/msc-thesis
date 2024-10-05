    long long result=1;
    for (int i=n;i>0;i--)
    {
        result*=i;
        if (i>1){
            for (int j=i-1;j>0;j--)
            {
                result*=j;
            }
        }
    }
    return result;
}   


