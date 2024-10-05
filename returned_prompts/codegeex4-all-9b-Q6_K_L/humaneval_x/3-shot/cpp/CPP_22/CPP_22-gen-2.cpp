    vector<int> all_ints;
    int i;
    for (i=0;i<values.size();i++)
    {
    if (boost::any_cast<int>(values[i])!=NULL)
    all_ints.push_back(boost::any_cast<int>(values[i]));
    }
    return all_ints;
}

