    map<char,int> count;
    int i;
    for(i=0;i<test.length();i++){
        count[test[i]]++;
    }
    int max_count = 0;
    for(auto it = count.begin(); it != count.end(); ++it){
        if(it->second > max_count){
            max_count = it->second;
        }
    }
    map<char,int> result;
    for(auto it = count.begin(); it != count.end(); ++it){
        if(it->second == max_count){
            result[it->first] = it->second;
        }
    }
    return result;
}


