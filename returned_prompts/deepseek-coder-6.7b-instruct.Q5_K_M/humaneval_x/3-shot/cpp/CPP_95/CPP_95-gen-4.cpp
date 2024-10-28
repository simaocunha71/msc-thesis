    bool all_lower=true;
    bool all_upper=true;
    for(auto it=dict.begin();it != dict.end();it++){
        for(auto c : it->first){
            if(!islower(c))
                all_lower=false;
            if(!isupper(c))
                all_upper=false;
        }
    }
    return all_lower || all_upper;
}


