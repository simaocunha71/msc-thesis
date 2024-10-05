    vector<int> ints;
    list_any::iterator it;
    for (it=values.begin();it!=values.end();it++)
        if (boost::any_cast<int>(*it)!=NULL)
            ints.push_back(boost::any_cast<int>(*it));
    return ints;
}



