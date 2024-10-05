    int i,j;
    for (i=lst.size()-1;i>=0;i--)
    if (lst[i]>=i+1)
    return i+1;
    return -1;
}


