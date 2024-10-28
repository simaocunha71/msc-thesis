    int sum=0;
    for (int i=0;i<q.size();i++)
    sum+=q[i];
    if (sum>w)
    return false;
    for (int i=0;i<q.size();i++)
    for (int j=i+1;j<q.size();j++)
    if (q[i]==q[j])
    return false;
    return true;
}



