    int max_unique=0;
    string max_word;
    for(auto word:words){
        vector<int> freq(26,0);
        for(char c:word)
            freq[c-'a']++;
        int unique=0;
        for(int i:freq)
            if(i>0)
                unique++;
        if(unique>max_unique||(unique==max_unique&&word<max_word)){
            max_unique=unique;
            max_word=word;
        }
    }
    return max_word;
}


