    map<char,int> count;
    int max_count=0;
    for(char & c : test){
        if(c != ' '){
            count[c]++;
            if(count[c] > max_count) max_count = count[c];
        }
    }
    map<char,int> result;
    for(auto & it : count)
        if(it.second == max_count)
            result[it.first] = it.second;
    return result;
}


