    bool all_upper = true, all_lower = true;
    for(auto const& pair: dict){
        for(auto const& chr: pair.first){
            if(!isupper(chr))
                all_upper = false;
            if(!islower(chr))
                all_lower = false;
        }
        if(!all_upper && !all_lower)
            return false;
        all_upper = true;
        all_lower = true;
    }
    return true;
}


