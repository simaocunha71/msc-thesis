    bool all_lower = true;
    bool all_upper = true;
    for(auto & kv : dict) {
        for(auto & c : kv.first) {
            if(!isupper(c))
                all_upper = false;
            if(!islower(c))
                all_lower = false;
        }
    }
    return all_lower || all_upper;
}


