    vector<int> result;
    list_any::iterator i;
    for (i=values.begin();i!=values.end();i++)
    if (boost::any_cast<int>(*i)!=NULL)
    result.push_back(boost::any_cast<int>(*i));

    return result;
}


