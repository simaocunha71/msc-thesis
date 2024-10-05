    map<char,int> hist;
    for(char& c : test){
        if(c == ' ') continue;
        hist[c]++;
    }
    int max_count = 0;
    for(auto& p : hist) max_count = max(max_count, p.second);
    map<char,int> result;
    for(auto& p : hist) if(p.second == max_count) result[p.first] = p.second;
    return result;
}


