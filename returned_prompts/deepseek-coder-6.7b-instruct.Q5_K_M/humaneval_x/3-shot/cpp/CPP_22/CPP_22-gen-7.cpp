    vector<int> integers;
    for(list_any::iterator it = values.begin(); it != values.end(); ++it)
    {
        if(boost::any_cast<int>(&(*it)))
            integers.push_back(boost::any_cast<int>(*it));
    }
    return integers;
}


