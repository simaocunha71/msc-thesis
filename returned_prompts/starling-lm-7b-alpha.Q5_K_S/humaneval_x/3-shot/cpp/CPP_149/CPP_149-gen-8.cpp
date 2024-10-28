    vector<string> result;
    int i;
    for (i=0;i<lst.size();i++)
    if (lst[i].length()%2==0)
    result.push_back(lst[i]);

    sort(result.begin(),result.end());
    return result;
}



