    int i;
    for (i=1;i<l.size();i++)
    if (l[i-1]>l[i])
        return false;
    return true;
}

