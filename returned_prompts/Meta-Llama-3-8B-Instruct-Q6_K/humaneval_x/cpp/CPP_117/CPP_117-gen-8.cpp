    vector<string> result;
    for(int i = 0; i < s.length(); i++){
        string word = "";
        while(i < s.length() && s[i] != ' '){
            word += s[i];
            i++;
        }
        int count = 0;
        for(int j = 0; j < word.length(); j++){
            if(word[j] != ' ' && word[j] != ' ' && isalpha(word[j])){
                count++;
            }
        }
        if(count == n){
            result.push_back(word);
        }
    }
    return result;
}

B:
    vector<string> select_words(string s,int n){
        vector<string> result;
        vector<string> words;
        string word = "";
        for(int i = 0; i < s.length(); i++){
            if(s[i] != ' '){
                word += s[i];
            }else{
                words.push_back(word);
                word = "";
            }
        }
        words.push_back(word);
        for(int i = 0; i < words.size(); i++){
            int count = 0;
            for(int j = 0; j < words[i].length(); j++){
                if(isalpha(words[i][j]) && words[i][j] != ' '){
                    count++;
                }
            }
            if(count == n){
                result.push_back(words[i]);
            }
        }
        return result;
    }

C:
    vector<string> select_words(string s,int n){
        vector<string> result;
        vector<string> words;
        string word = "";
        for(int i = 0; i < s.length(); i++){
            if(s[i] != ' '){
                word += s[i];
            }else{
                words.push_back(word);
                word = "";
            }
        }
        words.push_back(word);
        sort(words.begin(), words.end());
        for(int i = 0; i < words.size(); i++){
            int count = 0;
            for(int j = 0; j < words[i].length(); j++){
                if(isalpha(words[i][j]) && words[i][j] != ' '){
                    count++;
                }
            }
            if(count == n){
                result.push_back(words[i]);
            }
        }
        return result;
    }

D:
    vector<string> select_words(string s,int n){
        vector<string> result;
        vector<string> words;
        string word = "";
        for(int i = 0