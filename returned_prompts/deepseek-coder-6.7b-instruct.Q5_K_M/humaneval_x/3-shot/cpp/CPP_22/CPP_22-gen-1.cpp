    vector<int> result;
    for(auto it = values.begin(); it != values.end(); ++it)
    {
        if(boost::any_cast<int>(&*it)) 
        {
            result.push_back(boost::any_cast<int>(*it));
        }
    }
    return result;
}


