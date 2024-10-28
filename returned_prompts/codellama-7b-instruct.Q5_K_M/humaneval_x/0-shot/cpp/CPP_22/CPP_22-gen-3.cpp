    vector<int> ret;
    for(auto& x : values){
        if(x.type() == typeid(int)){
            ret.push_back(boost::any_cast<int>(x));
        }
    }
    return ret;
}
