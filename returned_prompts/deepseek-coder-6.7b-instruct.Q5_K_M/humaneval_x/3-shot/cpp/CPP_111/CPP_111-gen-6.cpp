    map<char, int> letter_map;
    for(char& c : test){
        if(c != ' '){
            letter_map[c]++;
        }
    }
    int max = 0;
    for(auto& it : letter_map){
        if(it.second > max){
            max = it.second;
        }
    }
    map<char, int> result;
    for(auto& it : letter_map){
        if(it.second == max){
            result.insert(it);
        }
    }
    return result;
}


