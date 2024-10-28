    vector<int> result;
    list_any::iterator it;
    for (it=values.begin();it!=values.end();it++)
    if (boost::any_cast<int>(*it) >= 0){
        result.push_back(boost::any_cast<int>(*it));
    }
    return result;
}


