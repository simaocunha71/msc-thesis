    sort(lst.begin(),lst.end());
    vector<int> odd;
    vector<int> even;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if (i%2==0)
        odd.push_back(lst[i]);
        else
        even.push_back(lst[i]);
    }
    for (i=0;i<odd.size();i++)
    {
        lst[i]=odd[i];
    }
    for (i=0;i<even.size();i++)
    {
        lst[i+odd.size()]=even[i];
    }
    return lst;
}

