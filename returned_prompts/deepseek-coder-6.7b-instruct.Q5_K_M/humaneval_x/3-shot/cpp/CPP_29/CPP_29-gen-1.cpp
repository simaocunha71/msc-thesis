    vector<string> result;
    for(auto &str : strings)
    {
        if(str.find(prefix) == 0) 
        {
            result.push_back(str);
        }
    }
    return result;
}


