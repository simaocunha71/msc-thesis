    sort(lst.begin(),lst.end());
    vector<string> result;
    int i;
    for (i=0;i<lst.size();i++)
    if (lst[i].size()%2==0){
        result.push_back(lst[i]);
    }
    return result;
}



