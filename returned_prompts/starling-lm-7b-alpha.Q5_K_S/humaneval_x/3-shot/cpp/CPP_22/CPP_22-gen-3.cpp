    vector<int> result;
    boost::any value;
    for (list_any::iterator it=values.begin();it!=values.end();it++)
    {
        value=*it;
        if (value.type()==TYPE_INT)
        result.push_back(boost::any_cast<int>(value));
    }
    return result;
}




