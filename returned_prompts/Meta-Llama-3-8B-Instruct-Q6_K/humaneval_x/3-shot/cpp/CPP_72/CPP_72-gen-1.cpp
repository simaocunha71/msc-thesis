    int sum=0;
    bool balanced=true;
    for (int i=0;i<q.size();i++)
    {
        sum+=q[i];
        if (i!=q.size()-i-1)
        {
            balanced=false;
        }
    }
    if (!balanced)
    {
        return false;
    }
    if (sum<=w)
    {
        return true;
    }
    return false;
}
