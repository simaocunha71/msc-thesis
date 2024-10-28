    int sum=0;
    for (int i=0;i<q.size();i++)
    sum+=q[i];
    if (sum>w)
    return false;
    if (sum==w)
    return true;
    if (q.size()==1)
    return true;
    int i=0;
    int j=q.size()-1;
    for (i=0;i<q.size();i++)
    {
        if (q[i]!=q[j])
        return false;
        j--;
    }
    return true;
}

