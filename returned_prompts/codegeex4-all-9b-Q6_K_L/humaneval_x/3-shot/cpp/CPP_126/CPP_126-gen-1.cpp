    vector<int> temp=lst;
    sort(temp.begin(),temp.end());
    for (int i=0;i<lst.size();i++)
        if (lst[i]!=temp[i]) return false;
    return true;
}

