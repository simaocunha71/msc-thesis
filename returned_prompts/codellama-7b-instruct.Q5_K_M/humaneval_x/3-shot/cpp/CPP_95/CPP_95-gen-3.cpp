    if (dict.empty())
    return false;
    else{
        string key;
        bool flag=true;
        for (auto i=dict.begin();i!=dict.end();i++){
            key=i->first;
            if (flag){
                if (islower(key[0]))
                flag=true;
                else{
                    flag=false;
                }
            }
            else{
                if (islower(key[0]))
                return false;
                else{
                    flag=false;
                }
            }
        }
        if (flag)
        return true;
        else
        return false;
    }
}


