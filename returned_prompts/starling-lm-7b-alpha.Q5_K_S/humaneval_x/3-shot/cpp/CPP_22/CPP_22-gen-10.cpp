    vector<int> result;
    for (list_any::iterator iter=values.begin();iter!=values.end();iter++)
    if (boost::any_cast<int>(*iter)>=0)
    result.push_back(boost::any_cast<int>(*iter));

    return result;
}


