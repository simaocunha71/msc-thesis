    vector<string> sorted;
    vector<string> sorted_copy;
    sort(lst.begin(), lst.end());
    for (int i=0;i<lst.size();i++)
    if (lst[i].length()%2==0)
    sorted.push_back(lst[i]);
    return sorted;
}


