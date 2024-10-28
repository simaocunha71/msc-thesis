    int i;
    int total=0;
    for (i=0;i<lst.size();i++)
    {
        total+=ceil(lst[i])*ceil(lst[i]);
    }
    return total;
}

