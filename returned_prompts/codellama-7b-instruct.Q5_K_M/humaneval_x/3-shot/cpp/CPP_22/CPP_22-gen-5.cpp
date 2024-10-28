    vector<int> result;
    list_any::iterator iter;
    for (iter=values.begin();iter!=values.end();iter++)
    if ((*iter).type()==typeid(int))
    result.push_back(boost::any_cast<int>(*iter));
    return result;
}


