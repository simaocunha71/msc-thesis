    int max_unique = 0;
    string max_word;
    for(string word : words){
        int unique = unique_count(word);
        if(unique > max_unique){
            max_unique = unique;
            max_word = word;
        }
        else if(unique == max_unique && word < max_word){
            max_word = word;
        }
    }
    return max_word;
}

int unique_count(string word){
    int count = 0;
    sort(word.begin(), word.end());
    for(int i = 0; i < word.length(); i++){
        if(i == 0 || word[i] != word[i-1]) count++;
    }
    return count;
}

