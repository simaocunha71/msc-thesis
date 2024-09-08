    map<char,int> result;
    if(test.empty()) return result;
    string::iterator it;
    for(it=test.begin();it!=test.end();++it){
        char c = *it;
        if(result.find(c) == result.end()) result[c] = 1;
        else result[c]++;
    }
    int max = 0;
    for(it=result.begin();it!=result.end();++it){
        if(it->second > max) max = it->second;
    }
    map<char,int> max_map;
    for(it=result.begin();it!=result.end();++it){
        if(it->second == max) max_map[it->first] = it->second;
    }
    return max_map;
}
