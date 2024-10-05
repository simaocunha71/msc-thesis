    int i;
    int j;

    for (i=0;i<lst.size();i++)
    for (j=i+1;j<lst.size();j++)
    {
        if (lst[i]>lst[j])
        return false;
    }
    return true;
}

