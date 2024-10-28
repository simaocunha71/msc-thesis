    int max_unique = 0;
    string max_word = "";

    for(string word : words){
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
    int count = 0;
    vector<bool> used(26, false);

    for(char c : word){
        if(!used[c - 'a']){
            used[c - 'a'] = true;
            count++;
        }
    }

    return count;
}

