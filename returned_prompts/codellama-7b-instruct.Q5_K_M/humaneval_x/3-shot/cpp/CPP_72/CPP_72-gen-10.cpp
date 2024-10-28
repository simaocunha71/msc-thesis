    int sum=0;
    bool balanced=true;
    for (int i=0;i<q.size();i++)
    {
        sum+=q[i];
        if (q[i]!=q[q.size()-i-1])
        balanced=false;
    }
    if (sum>w)
    return false;
    if (balanced)
    return true;
    return false;
}



