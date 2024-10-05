    map<char,int> counts;
    int max_count = 0;
    for(char c : test){
        if(c == ' ') continue;
        counts[c]++;
        if(counts[c] > max_count) max_count = counts[c];
    }
    map<char,int> result;
    for(auto &pair : counts){
        if(pair.second == max_count) result[pair.first] = pair.second;
    }
    return result;
}


