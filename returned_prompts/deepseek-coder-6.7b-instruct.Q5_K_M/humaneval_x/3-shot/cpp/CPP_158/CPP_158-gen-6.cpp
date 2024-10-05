    string max_word="";
    int max_unique=0;
    for(string word:words){
        sort(word.begin(),word.end());
        int unique_char=0;
        for(int i=0;i<word.size();i++){
            if(i==0||word[i]==word[i-1])
                continue;
            unique_char++;
        }
        if(unique_char>max_unique){
            max_unique=unique_char;
            max_word=word;
        }
        else if(unique_char==max_unique){
            max_word=min(max_word,word);
        }
    }
    return max_word;
}


