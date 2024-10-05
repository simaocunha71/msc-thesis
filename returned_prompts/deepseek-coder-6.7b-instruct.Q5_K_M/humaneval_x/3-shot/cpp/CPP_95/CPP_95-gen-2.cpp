    bool lower = true, upper = true;
    for(auto it = dict.begin(); it != dict.end(); it++){
        for(auto c: it->first){
            if(islower(c))
                upper = false;
            if(isupper(c))
                lower = false;
        }
    }
    return lower || upper;
}


