    int i;
    int prev;
    prev=lst[0];
    for (i=1;i<lst.size();i++)
    {
        if (lst[i]<prev)
        return false;
        prev=lst[i];
    }
    return true;
}

