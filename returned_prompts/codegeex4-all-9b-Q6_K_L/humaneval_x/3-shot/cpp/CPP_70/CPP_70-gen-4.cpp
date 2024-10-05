    sort(lst.begin(),lst.end());
    int i=0;
    vector<int> new_lst;
    while (i<lst.size())
    {
        new_lst.push_back(lst[i]);
        i+=2;
    }
    i=1;
    while (i<lst.size())
    {
        new_lst.push_back(lst[i]);
        i+=2;
    }
    return new_lst;
}