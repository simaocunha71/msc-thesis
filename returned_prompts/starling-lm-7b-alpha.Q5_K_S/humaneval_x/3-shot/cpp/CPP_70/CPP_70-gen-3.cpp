    vector<int> result;
    vector<int>::iterator it;
    int i,n;
    n=lst.size();
    for (i=0;i<n;i++)
    {
        it=min_element(lst.begin(),lst.end());
        result.push_back(*it);
        lst.erase(it);
        if (lst.size()==0)
        break;
        it=max_element(lst.begin(),lst.end());
        result.push_back(*it);
        lst.erase(it);
    }
    return result;
}



