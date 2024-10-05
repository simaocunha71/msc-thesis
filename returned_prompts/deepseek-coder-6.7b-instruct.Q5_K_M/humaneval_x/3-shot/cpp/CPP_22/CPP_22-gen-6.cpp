    vector<int> result;
    for(boost::any item : values)
    {
        if(boost::any_cast<int>(&item))
        {
            result.push_back(boost::any_cast<int>(item));
        }
    }
    return result;
}

