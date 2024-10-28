    vector<int> result;
    sort(lst.begin(),lst.end());
    int min=lst[0];
    int max=lst[lst.size()-1];
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]==min)
        {
            result.push_back(max);
            lst.erase(lst.begin()+i);
            i=-1;
        }
    }
    for (int i=0;i<lst.size();i++)
    {
        result.push_back(lst[i]);
    }
    return result;
}


