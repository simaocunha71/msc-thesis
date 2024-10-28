    vector<string> words;
    vector<string> result;
    string temp="";
    string consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            words.push_back(temp);
            temp="";
        }else{
            temp+=s[i];
        }
    }
    words.push_back(temp);
    for(int i=0;i<words.size();i++){
        int cnt=0;
        for(int j=0;j<words[i].size();j++){
            if(consonants.find(words[i][j])<words[i].size()){
                cnt++;
            }
        }
        if(cnt==n){
            result.push_back(words[i]);
        }
    }
    return result;
}


