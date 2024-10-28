    int max_unique = 0;
    string max_word;
    for(string word: words){
        vector<int> count(256, 0);
        int unique = 0;
        for(char c: word)
            if(count[c]++ == 0)
                unique++;
        if(unique > max_unique || (unique == max_unique && word < max_word)){
            max_unique = unique;
            max_word = word;
        }
    }
    return max_word;
}


