    vector<int> int_values;
    list_any::iterator it;
    for (it=values.begin();it!=values.end();it++)
    {
        if (boost::any_cast<int>(*it))
        int_values.push_back(boost::any_cast<int>(*it));
    }
    return int_values;
}



