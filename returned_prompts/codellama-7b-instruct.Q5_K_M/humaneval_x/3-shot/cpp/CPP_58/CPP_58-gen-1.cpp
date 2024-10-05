    vector<int> result;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    vector<int>::iterator it1=l1.begin(),it2=l2.begin(),it3;
    while (it1!=l1.end())
    {
        it3=find(l2.begin(),l2.end(),*it1);
        if (it3!=l2.end())
        {
            result.push_back(*it1);
            it1=find(it1+1,l1.end(),*it1);
            it2=find(it2+1,l2.end(),*it1);
        }
        else
            it1++;
    }
    sort(result.begin(),result.end());
    result.erase(unique(result.begin(),result.end()),result.end());
    return result;
}


