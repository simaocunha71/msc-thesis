    if (lst.size()<=1)
    return true;
    if (lst.size()>1)
    {
        int i;
        for (i=0;i<lst.size()-1;i++)
        if (lst[i]>lst[i+1])
        return false;
    }
    return true;
}


