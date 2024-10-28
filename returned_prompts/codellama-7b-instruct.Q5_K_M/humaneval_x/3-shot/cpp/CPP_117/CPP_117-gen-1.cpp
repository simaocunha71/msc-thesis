    vector<string> words;
    int i,j;
    string word;
    for (i=0;i<s.length();i++){
        if (s[i]!=' '){
            word+=s[i];
            if (s[i+1]==' '){
                words.push_back(word);
                word="";
            }
        }
        else{
            if (word.length()==n){
                words.push_back(word);
                word="";
            }
        }
    }
    if (word.length()==n){
        words.push_back(word);
        word="";
    }
    return words;
}


