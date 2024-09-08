    vector<float> l_prime;
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            int j = 0;
            for(int k = 0; k < l.size(); k++){
                if(k % 2 == 0){
                    j++;
                }
            }
            vector<float> even;
            for(int k = 0; k < l.size(); k++){
                if(k % 2 == 0){
                    even.push_back(l[k]);
                }
            }
            sort(even.begin(), even.end());
            l_prime.push_back(even[j-1]);
        }else{
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;
}

B:
    vector<float> l_prime;
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            vector<float> even;
            for(int j = 0; j < l.size(); j++){
                if(j % 2 == 0){
                    even.push_back(l[j]);
                }
            }
            sort(even.begin(), even.end());
            l_prime.push_back(even[0]);
        }else{
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;

C:
    vector<float> l_prime;
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            sort(vector<float>(l.begin(), l.begin() + l.size()).begin() + i, vector<float>(l.begin(), l.begin() + l.size()).begin() + i + 1);
            l_prime.push_back(vector<float>(l.begin(), l.begin() + l.size()).begin() + i);
        }else{
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;
}

D:
    vector<float> l_prime;
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            auto it = std::min_element(l.begin(), l.end());
            l_prime.push_back(*it);
        }else{
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;

E:
    vector<float> l_prime;
    for(int i = 0; i < l.size(); i++){
        if(i % 2 == 0){
            sort(l.begin(), l.end());
            l