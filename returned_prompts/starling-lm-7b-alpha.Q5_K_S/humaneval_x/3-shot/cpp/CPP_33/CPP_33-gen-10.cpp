    vector<int> result;
    vector<int>::iterator third_itr;
    for (third_itr=l.begin();third_itr!=l.end();third_itr++)
    if ((*third_itr)%3==0)
    result.push_back(*third_itr);
    sort(result.begin(),result.end());
    for (third_itr=l.begin();third_itr!=l.end();third_itr++)
    if ((*third_itr)%3!=0)
    result.push_back(*third_itr);
    return result;
}


