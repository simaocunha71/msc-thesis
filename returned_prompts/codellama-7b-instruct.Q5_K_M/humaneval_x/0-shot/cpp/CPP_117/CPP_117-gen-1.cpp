    vector<string> words;
    if(s.empty())
        return words;
    //split into words
    int start = 0;
    int end;
    for(int i = 0; i<s.size(); i++){
        if(s[i] == ' '){
            end = i-1;
            words.push_back(s.substr(start,end-start+1));
            start = i+1;
        }
    }
    end = s.size()-1;
    words.push_back(s.substr(start,end-start+1));
    //filter
    vector<string> res;
    for(int i = 0; i<words.size(); i++){
        int cnt = 0;
        for(int j = 0; j<words[i].size(); j++){
            if(words[i][j] != ' ' && words[i][j] != '\0'){
                if(cnt++ < n)
                    res.push_back(words[i]);
                else
                    break;
            }
        }
    }
    return res;
}

/*
