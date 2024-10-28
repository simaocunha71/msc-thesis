    string max_word = "";
    int max_unique = 0;
    for(string word: words){
        vector<int> count(256, 0);
        for(char chr: word){
            count[chr]++;
        }
        int unique = 0;
        for(int i=0;i<256;i++){
            if(count[i]>0) unique++;
        }
        if(unique>max_unique || (unique==max_unique && word<max_word)){
            max_word = word;
            max_unique = unique;
        }
    }
    return max_word;
}


