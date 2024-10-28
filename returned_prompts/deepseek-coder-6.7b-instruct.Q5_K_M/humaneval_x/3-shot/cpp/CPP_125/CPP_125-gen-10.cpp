    vector<string> words;
    size_t pos = 0;
    string token;
    string delimiter = " ";
    if(txt.find(delimiter) == string::npos) delimiter = ",";
    if(txt.find(delimiter) == string::npos){
        int count = 0;
        for(char c : txt) if(islower(c) && (c-'a')%2 != 0) count++;
        return {to_string(count)};
    }
    while ((pos = txt.find(delimiter)) != string::npos) {
        token = txt.substr(0, pos);
        words.push_back(token);
        txt.erase(0, pos + delimiter.length());
    }
    words.push_back(txt);
    return words;
}


