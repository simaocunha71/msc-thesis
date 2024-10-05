    int max_unique = -1;
    string max_word;
    for(auto word : words){
        int unique = unique_count(word);
        if(unique > max_unique){
            max_unique = unique;
            max_word = word;
        }
        else if(unique == max_unique){
            if(word < max_word){
                max_word = word;
            }
        }
    }
    return max_word;
}

int unique_count(string word){
    sort(word.begin(), word.end());
    int count = 1;
    for(int i = 1; i < word.size(); i++){
        if(word[i] != word[i-1]){
            count++;
        }
    }
    return count;
}

