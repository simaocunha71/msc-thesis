    vector<string> result;
    int i = 0;
    while(i < paren_string.size()) {
        int count = 0;
        int start = i;
        while(i < paren_string.size() && paren_string[i] != '(' && paren_string[i] != ')') {
            i++;
        }
        if(i < paren_string.size() && paren_string[i] == '(') {
            i++;
            count++;
            while(i < paren_string.size() && paren_string[i] != ')') {
                i++;
            }
            if(i < paren_string.size() && paren_string[i] == '(') {
                i++;
                count++;
                while(i < paren_string.size() && paren_string[i] != ')') {
                    i++;
                }
            }
        }
        string temp = paren_string.substr(start, i - start);
        result.push_back(temp);
    }
    return result;
}

