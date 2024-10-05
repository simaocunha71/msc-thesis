    vector<int> result;
    for(auto value : values)
    {
        try
        {
            int i = boost::any_cast<int>(value);
            result.push_back(i);
        }
        catch(boost::bad_any_cast)
        {
            continue;
        }
    }
    return result;
}

