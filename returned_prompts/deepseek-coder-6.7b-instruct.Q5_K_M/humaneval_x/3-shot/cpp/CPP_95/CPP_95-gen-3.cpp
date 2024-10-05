    bool lower=true, upper=true;
    for(auto const& x: dict){
        for(auto const& c: x.first){
            if(isupper(c)) lower=false;
            if(islower(c)) upper=false;
        }
    }
    return lower||upper;
}

