    vector<int> ints;
    for(list_any::iterator it=values.begin();it!=values.end();it++){
        if (typeid(int)==typeid(*it)){
            ints.push_back(boost::any_cast<int>(*it));
        }
    }
    return ints;
}



