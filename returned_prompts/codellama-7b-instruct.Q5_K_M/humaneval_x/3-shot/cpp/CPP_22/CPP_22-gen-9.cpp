    vector<int> ints;
    for (int i=0;i<values.size();i++)
    {
        if (values[i].type()==typeid(int))
        ints.push_back(boost::any_cast<int>(values[i]));
    }
    return ints;
}


