    vector<string> words;
    vector<string> result;
    string word="";
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            words.push_back(word);
            word="";
        }
        else{
            word+=s[i];
        }
    }
    words.push_back(word);
    for(int i=0;i<words.size();i++){
        int count=0;
        for(int j=0;j<words[i].size();j++){
            char c=tolower(words[i][j]);
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'){
                count++;
            }
        }
        if(count==n){
            result.push_back(words[i]);
        }
    }
    return result;
}


