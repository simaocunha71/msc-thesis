    int sum=0;
    bool balanced=true;
    int i;
    for (i=0;i<q.size();i++)
    {
        sum+=q[i];
        if (q[i]!=q[q.size()-i-1])
        balanced=false;
    }
    if (sum<=w && balanced)
    return true;
    return false;
}


