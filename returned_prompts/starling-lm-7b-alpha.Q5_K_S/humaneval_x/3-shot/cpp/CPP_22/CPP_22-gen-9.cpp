    vector<int> result;
    boost::any value;
    list_any::iterator it;
    for (it=values.begin();it!=values.end();it++)
    {
        value=*it;
        if (value.type()==typeid(int).name())
        {
            result.push_back(value.convert<int>());
        }
    }
    return result;
}



