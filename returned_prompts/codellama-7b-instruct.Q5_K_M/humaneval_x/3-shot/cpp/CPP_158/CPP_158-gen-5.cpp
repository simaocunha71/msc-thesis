    sort(words.begin(), words.end());
    int n=words.size();
    int max_unique=0;
    string max_word;
    for (int i=0;i<n;i++){
        int count=0;
        string word=words[i];
        for (int j=0;j<word.length();j++){
            if (word[j]!=word[j+1])
            count+=1;
        }
        if (count>max_unique){
            max_unique=count;
            max_word=word;
        }
    }
    return max_word;
}


