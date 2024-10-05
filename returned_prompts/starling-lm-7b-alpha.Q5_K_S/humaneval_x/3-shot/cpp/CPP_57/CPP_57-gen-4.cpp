    int i;
    for (i=0;i<l.size();i++)
    if (i>0 && (l[i]>=l[i-1] || l[i]<=l[i-1]))
    return false;
    return true;
}


