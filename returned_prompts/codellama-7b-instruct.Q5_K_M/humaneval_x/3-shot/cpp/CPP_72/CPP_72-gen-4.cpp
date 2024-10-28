    int i;
    for (i=0;i<q.size();i++)
    if (q[i]>=w)
    return false;
    if (q.size()==1)
    return true;
    for (i=0;i<q.size()/2;i++)
    if (q[i]!=q[q.size()-1-i])
    return false;
    return true;
}



