    vector<int> all_integers;
    for (boost::any value:values)
    if (value.type()==typeid(int))
    {
        all_integers.push_back(value.convert<int>());
    }
    return all_integers;
}



