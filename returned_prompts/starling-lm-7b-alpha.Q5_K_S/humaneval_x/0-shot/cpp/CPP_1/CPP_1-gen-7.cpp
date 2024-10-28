    vector<string> ret;
    while(paren_string.size()){
        paren_string = separate_paren_groups_rec(paren_string);
    }
    return ret;
}

string separate_paren_groups_rec(string& paren_string){
    char c = paren_string[0];
    if(c == '('){
        paren_string = paren_string.substr(1);
        string ret;
        while(paren_string.size() && paren_string[0] == '('){
            paren_string = paren_string.substr(1);
            ret += '(';
        }
        if(paren_string.size()){
            ret += paren_string;
        }
        p