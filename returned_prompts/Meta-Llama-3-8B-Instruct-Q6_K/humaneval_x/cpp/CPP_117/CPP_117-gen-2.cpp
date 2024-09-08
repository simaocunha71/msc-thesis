    vector<string> result;
    int count = 0;
    string word = "";
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            word += s[i];
            if(!isalpha(s[i+1]) || i == s.length()-1){
                if(count == n){
                    result.push_back(word);
                }
                count = 0;
                word = "";
            }else{
                if(!isalpha(s[i+1])){
                    count++;
                }
            }
        }
    }
    return result;
}

