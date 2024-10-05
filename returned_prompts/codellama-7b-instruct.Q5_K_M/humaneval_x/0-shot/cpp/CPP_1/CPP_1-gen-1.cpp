    vector<string> ret;
    int open_count = 0;
    string cur = "";
    for(int i = 0; i < paren_string.size(); ++i){
        if(paren_string[i] == '(')
            ++open_count;
        else if(paren_string[i] == ')')
            --open_count;
        cur += paren_string[i];
        if(open_count == 0){
            ret.push_back(cur);
            cur = "";
        }
    }
    return ret;
}

