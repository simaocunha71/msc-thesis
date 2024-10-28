    int i;
    vector<string> v1;
    for (i=0;i<lst.size();i++)
    if (lst[i].length()%2==0)
    v1.push_back(lst[i]);
    sort(v1.begin(),v1.end());
    return v1;
}

