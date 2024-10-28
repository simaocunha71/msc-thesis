    vector<int> ints;
    for  (auto it = values.begin(); it != values.end(); ++it)
    {
        if  (boost::any_cast<int>(&(*it)))
        {
            ints.push_back(boost::any_cast<int>((*it)));
        }
    }
    return ints;
}


