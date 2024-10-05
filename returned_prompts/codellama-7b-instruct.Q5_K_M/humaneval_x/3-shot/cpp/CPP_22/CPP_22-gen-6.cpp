    vector<int> filtered;
    list_any::iterator it;
    for (it=values.begin();it!=values.end();it++)
    if (boost::any_cast<int>(*it)!=0)
    filtered.push_back(boost::any_cast<int>(*it));
    return filtered;
}



