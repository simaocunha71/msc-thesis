    int i;
    int total=0;
    for (i=0;i<q.size();i++)
    total+=q[i];

    if (total>w)
    return false;

    for (i=0;i<q.size();i++)
    if (q[i]!=q[q.size()-i-1])
    return false;

    return true;
}



