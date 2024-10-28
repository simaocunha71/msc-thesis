    int i,cnt=0,div;
    for (i=1;i<n;i++)
    {
        div=i%11;
        if (div==0 || div==2)
        {
            if (i%13==0 && i%10==7)
            cnt+=1;
        }
    }
    return cnt;
}


