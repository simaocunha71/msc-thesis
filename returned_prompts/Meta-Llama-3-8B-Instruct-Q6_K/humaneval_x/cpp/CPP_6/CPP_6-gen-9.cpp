    vector<int> result;
    int level = 0;
    for(int i = 0; i < paren_string.length(); i++) {
        if(paren_string[i] == '(') {
            level++;
        } else if(paren_string[i] == ')') {
            level--;
        }
        if(level == 0) {
            result.push_back(level);
        }
    }
    return result;
}

