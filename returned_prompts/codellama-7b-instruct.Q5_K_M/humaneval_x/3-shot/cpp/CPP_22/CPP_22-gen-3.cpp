    vector<int> ints;
    for (list_any::iterator it = values.begin(); it != values.end(); ++it)
    {
        if (typeid(*it)==typeid(int))
        {
            ints.push_back(boost::any_cast<int>(*it));
        }
    }
    return ints;
}


