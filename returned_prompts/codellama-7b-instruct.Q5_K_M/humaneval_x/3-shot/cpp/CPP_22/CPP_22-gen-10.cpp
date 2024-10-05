    vector<int> integers;
    for (int i=0;i<values.size();i++)
    if (boost::any_cast<int>(values[i]))
    integers.push_back(boost::any_cast<int>(values[i]));
    return integers;
}


