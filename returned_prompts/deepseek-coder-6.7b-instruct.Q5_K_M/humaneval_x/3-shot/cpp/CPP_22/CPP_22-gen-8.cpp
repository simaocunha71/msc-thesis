    vector<int> integers;
    for(auto value: values){
        if(boost::any_cast<int>(&value)!=nullptr)
            integers.push_back(boost::any_cast<int>(value));
    }
    return integers;
}


