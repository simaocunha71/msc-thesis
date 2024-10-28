    int sum=0;
    int i;
    for (i=0;i<q.size();i++)
    {
        sum+=q[i];
    }
    if (sum<=w)
    {
        int j;
        for (j=0;j<q.size()/2;j++)
        {
            if (q[j]!=q[q.size()-1-j])
            return false;
        }
        return true;
    }
    else
    return false;
}

