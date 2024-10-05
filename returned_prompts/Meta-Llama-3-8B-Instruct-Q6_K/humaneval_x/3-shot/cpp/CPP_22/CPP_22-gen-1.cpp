    vector<int> result;
    for (list_any::iterator it=values.begin();it!=values.end();it++)
    {
        if (typeid(*it).name() == "i")
        {
            result.push_back(boost::any_cast<int>(*it));
        }
    }
    return result;
}

