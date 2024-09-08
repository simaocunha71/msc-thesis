    vector<string> res;
    if(s.empty())
        return res;
    string word;
    for(int i=0;i<s.size();i++){
        if(s[i] == ' '){
            if(word.size() > n && isalpha(word[0])){
                res.push_back(word);
            }
            word = "";
        }
        else if(isalpha(s[i])){
            word += tolower(s[i]);
        }
    }
    if(word.size() > n && isalpha(word[0]))
        res.push_back(word);
    sort(res.begin(),res.end());
    return res;
}

B:
    vector<string> select_words(string s,int n){
        vector<string> res;
        if(s.empty())
            return res;
        string word;
        for(auto c : s){
            if(c == ' '){
                if(word.size() > n && isalpha(word[0])){
                    res.push_back(word);
                }
                word = "";
            }
            else if(isalpha(c)){
                word += tolower(c);
            }
        }
        if(word.size() > n && isalpha(word[0]))
            res.push_back(word);
        sort(res.begin(),res.end());
        return res;
    }

C:
    vector<string> select_words(string s,int n){
        vector<string> res;
        if(s.empty())
            return res;
        string word;
        for(int i=0;i<s.size();i++){
            if(s[i] == ' '){
                if(word.size() > n && isalpha(word[0])){
                    res.push_back(word);
                }
                word = "";
            }
            else if(isalpha(s[i])){
                if(islower(s[i]))
                    word += tolower(s[i]);
                else
                    word += s[i];
            }
        }
        if(word.size() > n && isalpha(word[0]))
            res.push_back(word);
        sort(res.begin(),res.end());
        return res;
    }

D:
    vector<string> select_words(string s,int n){
        vector<string> res;
        if(s.empty())
            return res;
        string word;
        for(int i=0;i<s.size();i++){
            if(s[i] == ' '){
                if(word.size() > n && isalpha(word[0])){
                    res.push_back(word);
                }
                word = "";
            }
            else if(isalpha(s[i])){
                word += tolower(s[i]);
            }
        }
        if(word.size() > n && isalpha(word[0