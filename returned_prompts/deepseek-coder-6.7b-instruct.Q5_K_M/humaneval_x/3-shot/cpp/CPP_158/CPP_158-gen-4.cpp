    int max_unique = -1;
    string max_word;
    for(auto &word: words){
        int unique = unique_count(word);
        if(unique > max_unique){
            max_unique = unique;
            max_word = word;
        }
        else if(unique == max_unique){
            max_word = min(max_word, word);
        }
    }
    return max_word;
}

int unique_count(string word){
    vector<bool> count(26, false);
    for(char c: word){
        count[c - 'a'] = true;
    }
    int unique = 0;
    for(bool b: count){
        unique += b;
    }
    return unique;
}


