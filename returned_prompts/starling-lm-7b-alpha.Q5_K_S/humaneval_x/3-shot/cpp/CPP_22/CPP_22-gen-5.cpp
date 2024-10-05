    vector<int> all_ints;
    int i;
    for (i=0;i<values.size();i++)
    if (values[i].type()==typeid(int))
    {
        all_ints.push_back(boost::any_cast<int>(values[i]));
    }
    return all_ints;
}


