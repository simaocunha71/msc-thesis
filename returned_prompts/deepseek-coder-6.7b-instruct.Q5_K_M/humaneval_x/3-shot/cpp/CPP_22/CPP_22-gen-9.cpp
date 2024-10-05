    vector<int> integers;
    for(auto i: values)
    {
        if(boost::any_cast<int>(&i)!=NULL)
        integers.push_back(boost::any_cast<int>(i));
    }
    return integers;
}


