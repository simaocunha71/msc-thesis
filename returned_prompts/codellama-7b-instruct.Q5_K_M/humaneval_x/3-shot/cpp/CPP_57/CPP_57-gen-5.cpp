    int i,j,n=l.size();
    float diff;
    if (n==0)
    return true;
    if (n==1)
    return true;
    for (i=0;i<n-1;i++)
    {
        diff=l[i+1]-l[i];
        if (diff>0)
        {
            for (j=i+2;j<n;j++)
            if (l[j]-l[i+1]>0)
            return false;
        }
        else if (diff<0)
        {
            for (j=i+2;j<n;j++)
            if (l[j]-l[i+1]<0)
            return false;
        }
        else
        return false;
    }
    return true;
}


