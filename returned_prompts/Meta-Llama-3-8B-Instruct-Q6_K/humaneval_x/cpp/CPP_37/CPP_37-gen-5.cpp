    vector<float> l_prime;

    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            // even indices, sort them
            vector<float> temp;
            for(int j = 0; j < l.size(); j++){
                if(j % 2 == 0){
                    temp.push_back(l[j]);
                }
            }
            sort(temp.begin(), temp.end());
            l_prime.push_back(temp[0]);
        }
        else{
            // odd indices, keep them as they are
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;
}

B:
    vector<float> l_prime;
    sort(l.begin(), l.end());
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            l_prime.push_back(l[i]);
        }
        else{
            l_prime.push_back(l[i-1]);
        }
    }
    return l_prime;
}

C:
    vector<float> l_prime;
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            // even indices, sort them
            vector<float> temp;
            for(int j = 0; j < l.size(); j++){
                if(j % 2 == 0){
                    temp.push_back(l[j]);
                }
            }
            sort(temp.begin(), temp.end());
            l_prime.push_back(temp[0]);
        }
        else{
            // odd indices, keep them as they are
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;
}C:
    vector<float> l_prime;
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            // even indices, sort them
            vector<float> temp;
            for(int j = 0; j < l.size(); j++){
                if(j % 2 == 0){
                    temp.push_back(l[j]);
                }
            }
            sort(temp.begin(), temp.end());
            l_prime.push_back(temp[0]);
        }
        else{
            // odd indices, keep them as they are
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;
}
D:
    vector<float> l_prime;
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
