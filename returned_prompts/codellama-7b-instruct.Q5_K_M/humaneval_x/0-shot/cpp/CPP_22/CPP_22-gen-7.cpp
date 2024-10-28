    vector<int> v;
    for(auto value : values){
        try{
            int x = boost::any_cast<int>(value);
            v.push_back(x);
        }
        catch(...){}
    }
    return v;
}
