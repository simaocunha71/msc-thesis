    vector<int> only_ints;
    int val;
    for (list_any::iterator it=values.begin();it!=values.end();it++)
    {
        val=boost::any_cast<int>(*it);
        only_ints.push_back(val);
    }

    return only_ints;
}


