    vector<string> result;
    // Split the string into words
    string word;
    for(int i=0; i<s.length(); i++){
        if(s[i] == ',' || s[i] == ' '){
            if(!word.empty()){
                result.push_back(word);
                word.clear();
            }
        }
        else{
            word += s[i];
        }
    }
    if(!word.empty()){
        result.push_back(word);
    }
    return result;
}

