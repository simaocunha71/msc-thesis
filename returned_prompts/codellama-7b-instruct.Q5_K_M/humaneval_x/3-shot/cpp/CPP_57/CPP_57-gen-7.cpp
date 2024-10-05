    int i;
    float val;
    if (l.size()==1)
    return true;
    if (l[0]==l[1])
    return true;
    if (l[0]==l[l.size()-2])
    return true;
    for (i=1;i<l.size()-1;i++)
    {
        if (l[i]>l[i+1])
        return false;
        if (l[i]<l[i+1])
        return true;
    }
    return true;
}


