    vector<string> result;
    size_t pos = 0, last_pos = 0;
    string delimiters = " ,";
    while(true){
        pos = txt.find_first_of(delimiters, last_pos);
        if(pos == string::npos) break;
        if(pos != last_pos){
            string word = txt.substr(last_pos, pos-last_pos);
            result.push_back(word);
        }
        last_pos = pos+1;
    }
    if(last_pos < txt.size()){
        string word = txt.substr(last_pos);
        result.push_back(word);
    }
    if(result.size()==1){
        int count = 0;
        for(char c: result[0]){
            if(islower(c) && (c-'a')%2 == 1) count++;
        }
        result.clear();
        result.push_back(to_string(count));
    }
    return result;
}


