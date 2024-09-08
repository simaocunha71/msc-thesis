    int max_count=0;
    string max_word="";
    for(int i=0; i<words.size(); i++){
        int count = 0;
        set<char> s;
        for(int j=0; j<words[i].size(); j++){
            if(s.find(words[i][j]) == s.end()){
                count++;
                s.insert(words[i][j]);
            }
        }
        if(count > max_count){
            max_count = count;
            max_word = words[i];
        }
    }
    return max_word;
}

B:
    int max_count=0;
    string max_word="";
    for(int i=0; i<words.size(); i++){
        int count = 0;
        set<char> s;
        for(int j=0; j<words[i].size(); j++){
            if(s.find(words[i][j]) == s.end()){
                count++;
                s.insert(words[i][j]);
            }
        }
        if(count > max_count){
            max_count = count;
            max_word = words[i];
        }
    }
    return max_word;
}

C:
    int max_count=0;
    string max_word="";
    for(int i=0; i<words.size(); i++){
        int count = 0;
        set<char> s;
        for(int j=0; j<words[i].size(); j++){
            if(s.find(words[i][j]) == s.end()){
                count++;
                s.insert(words[i][j]);
            }
        }
        if(count > max_count){
            max_count = count;
            max_word = words[i];
        }
    }
    return max_word;
}

D:
    int max_count=0;
    string max_word="";
    for(int i=0; i<words.size(); i++){
        int count = 0;
        set<char> s;
        for(int j=0; j<words[i].size(); j++){
            if(s.find(words[i][j]) == s.end()){
                count++;
                s.insert(words[i][j]);
            }
        }
        if(count > max_count){
            max_count = count;
            max_word = words[i];
        }
    }
    return max_word;
}

E:
    int max_count=0;
    string max_word="";
    for(int i=0; i<words.size(); i++){
        int count = 0;
        set<char> s;
        for(int j=0; j<words[i].size