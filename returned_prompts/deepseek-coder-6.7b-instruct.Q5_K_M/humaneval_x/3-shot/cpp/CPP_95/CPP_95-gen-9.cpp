    bool lower=true,upper=true;
    for(auto it=dict.begin();it !=dict.end();++it){
        for(auto c: it->first)
            if(islower(c)) upper=false;
            else lower=false;
        if(!upper&&lower) return true;
        upper=true;lower=true;
    }
    return false;
}

