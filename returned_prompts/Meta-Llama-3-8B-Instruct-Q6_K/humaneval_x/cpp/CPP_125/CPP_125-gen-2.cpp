    vector<string> result;
    int i = 0;
    while(i < txt.length()){
        if(txt[i] == ' '){
            result.push_back(txt.substr(i+1));
            i += 1;
        }
        else if(txt[i] == ','){
            result.push_back(txt.substr(i+1));
            i += 1;
        }
        else{
            int j = i+1;
            while(j < txt.length() && txt[j] != ' ' && txt[j] != ',') j++;
            result.push_back(txt.substr(i, j-i));
            i = j;
        }
    }
    return result;
}

B:
    if(txt.find(' ') == string::npos){
        int count = 0;
        for(int i = 0; i < 26; i++){
            if(txt.find((char)(97+i)) != string::npos) count++;
        }
        vector<string> result;
        result.push_back(to_string(count));
        return result;
    }else{
        vector<string> result;
        string word;
        for(char c : txt){
            if(c == ' '){
                result.push_back(word);
                word = "";
            }else word += c;
        }
        result.push_back(word);
        return result;
    }

C:
    int count = 0;
    for(int i = 0; i < 26; i++){
        if(txt.find((char)(97+i)) != string::npos) count++;
    }
    vector<string> result;
    result.push_back(to_string(count));
    return result; // this will return a vector with one element, the count of lower-case letters with odd order in the alphabet

D:
    string word;
    for(char c : txt){
        if(c == ' '){
            result.push_back(word);
            word = "";
        }else if(c == ','){
            result.push_back(word);
            word = "";
        }else word += c;
    }
    result.push_back(word);
    return result;

E:
    int count = 0;
    for(int i = 0; i < 26; i++){
        if(txt.find((char)(97+i)) != string::npos) count++;
    }
    vector<string> result;
    if(txt.find(' ') == string::npos) result.push_back(to_string(count));
    else{
        string word;
        for(char c : txt){
            if(c == ' '){
                result.push_back(word);
                word =