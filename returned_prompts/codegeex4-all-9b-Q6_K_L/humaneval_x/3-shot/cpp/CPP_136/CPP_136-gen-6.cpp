    vector<int> smallest_largest;
    int largest=0;
    int smallest=0;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0 && lst[i]>largest)
        largest=lst[i];
        if (lst[i]>0 && lst[i]<smallest)
        smallest=lst[i];
    }
    smallest_largest.push_back(largest);
    smallest_largest.push_back(smallest);
    return smallest_largest;
}

