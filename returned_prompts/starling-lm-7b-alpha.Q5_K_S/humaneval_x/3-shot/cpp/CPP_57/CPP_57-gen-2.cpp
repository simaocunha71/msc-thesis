    int i;
    for (i=1;i<l.size();i++)
    if (l[i]-l[i-1]>0)
    return false;

    for (i=1;i<l.size();i++)
    if (l[i-1]-l[i]>0)
    return false;

    return true;
}


