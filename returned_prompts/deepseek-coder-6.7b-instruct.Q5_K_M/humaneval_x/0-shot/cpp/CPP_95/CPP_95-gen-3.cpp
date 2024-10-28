    if(dict.empty())
        return false;
    else{
        bool lower = true, upper = true;
        for(auto &i : dict){
            for(auto &j : i.first){
                if(islower(j))
                    lower = false;
                else if(isupper(j))
                    upper = false;
            }
            if(lower == false && upper == false)
                return