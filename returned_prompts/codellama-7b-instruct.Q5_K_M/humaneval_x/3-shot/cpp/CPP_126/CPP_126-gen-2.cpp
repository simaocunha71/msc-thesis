    bool is_sorted=true;
    int i;
    for (i=0;i<lst.size()-1;i++)
    if (lst[i]>lst[i+1])
    is_sorted=false;

    return is_sorted;
}


