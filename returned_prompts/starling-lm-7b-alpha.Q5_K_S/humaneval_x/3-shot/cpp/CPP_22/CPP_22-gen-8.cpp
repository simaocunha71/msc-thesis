    vector<int> integers;
    boost::any any_value;
    for (list_any::iterator it=values.begin();it!=values.end();it++)
    {
        any_value=*it;
        if (any_value.type()==TYPE_INT){
            integers.push_back(boost::any_cast<int>(any_value));
        }
    }
    return integers;
}


