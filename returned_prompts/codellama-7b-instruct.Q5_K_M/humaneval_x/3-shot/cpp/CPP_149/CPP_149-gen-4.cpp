    vector<string> lst2;
    vector<string> lst3;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i].length()%2==0)
        lst3.push_back(lst[i]);
    }
    sort(lst3.begin(),lst3.end());
    return lst3;
}



