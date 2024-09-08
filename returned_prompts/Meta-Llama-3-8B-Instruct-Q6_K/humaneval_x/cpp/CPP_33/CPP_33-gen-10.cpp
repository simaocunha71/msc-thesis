    vector<int> l_prime = l;
    for(int i = 0; i < l_prime.size(); i++){
        if(i % 3 == 0){
            sort(l_prime.begin() + i, l_prime.begin() + i + 1);
        }
    }
    return l_prime;
}

B:
    vector<int> l_prime = l;
    for(int i = 0; i < l_prime.size(); i++){
        if(i % 3 == 0){
            vector<int> temp;
            for(int j = 0; j < l_prime[i]; j++){
                temp.push_back(j);
            }
            sort(temp.begin(), temp.end());
            l_prime[i] = temp[0];
        }
    }
    return l_prime;
}

C:
    vector<int> l_prime = l;
    for(int i = 0; i < l_prime.size(); i++){
        if(i % 3 == 0){
            l_prime[i] = *std::min_element(l_prime.begin() + i, l_prime.begin() + i + 1);
        }
    }
    return l_prime;
}

D:
    vector<int> l_prime = l;
    for(int i = 0; i < l_prime.size(); i++){
        if(i % 3 == 0){
            l_prime[i] = *std::max_element(l_prime.begin() + i, l_prime.begin() + i + 1);
        }
    }
    return l_prime;
}

E:
    vector<int> l_prime = l;
    for(int i = 0; i < l_prime.size(); i++){
        if(i % 3 == 0){
            l_prime[i] = *std::min_element(l_prime.begin(), l_prime.begin() + i + 1);
        }
    }
    return l_prime;
}

F:
    vector<int> l_prime = l;
    for(int i = 0; i < l_prime.size(); i++){
        if(i % 3 == 0){
            l_prime[i] = *std::max_element(l_prime.begin(), l_prime.begin() + i + 1);
        }
    }
    return l_prime;
}
