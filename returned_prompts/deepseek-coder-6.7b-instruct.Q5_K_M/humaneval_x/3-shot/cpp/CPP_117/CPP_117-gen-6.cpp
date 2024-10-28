    vector<string> words;
    vector<string> res;
    string temp="";
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            words.push_back(temp);
            temp="";
        }
        else{
            temp+=s[i];
        }
    }
    words.push_back(temp);
    for(int i=0;i<words.size();i++){
        int c=0;
        for(int j=0;j<words[i].size();j++){
            char ch=tolower(words[i][j]);
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
                c--;
            }
            else{
                c++;
            }
        }
        if(c==n){
            res.push_back(words[i]);
        }
    }
    return res;
}


