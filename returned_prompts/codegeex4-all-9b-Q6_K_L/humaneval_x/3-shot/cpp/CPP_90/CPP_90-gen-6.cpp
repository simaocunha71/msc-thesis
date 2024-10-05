    int n=lst.size();
    int second_smallest;
    if (n<2)
    return -1;
    sort(lst.begin(),lst.end());
    for (int i=1;i<n;i++)
    {
        if (lst[i]!=lst[i-1])
        {
            second_smallest=lst[i];
            break;
        }
    }
    return second_smallest;
}

