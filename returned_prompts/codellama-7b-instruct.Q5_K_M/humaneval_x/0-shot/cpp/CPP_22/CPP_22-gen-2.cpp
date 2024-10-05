    vector<int> result;
    for(auto it = values.begin(); it != values.end(); ++it){
        auto v = boost::any_cast<int>(*it);
        if(v != boost::none){
            result.push_back(v);
        }
    }
    return result;
}
