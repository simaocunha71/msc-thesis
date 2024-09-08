    vector<string> result;
    int open = 0;
    string current_group;

    for(int i = 0; i < paren_string.length(); i++){
        if(paren_string[i] == '('){
            open++;
            current_group += paren_string[i];
        }
        else if(paren_string[i] == ')'){
            current_group += paren_string[i];
            if(open > 0) open--;
            else{
                result.push_back(current_group);
                current_group = "";
            }
        }
    }
    if(open > 0) result.push_back(current_group);
    return result;
}

B:
    vector<string> separate_paren_groups(string s) {
        vector<string> result;
        string current = "";
        int open = 0;

        for (char c : s) {
            if (c == '(') {
                open++;
                current += c;
            } else if (c == ')') {
                current += c;
                if (--open == 0) {
                    result.push_back(current);
                    current = "";
                }
            }
        }
        return result;
    }

C:
    vector<string> separate_paren_groups(string s) {
        vector<string> result;
        string current = "";
        int open = 0;

        for (char c : s) {
            if (c == '(') {
                open++;
                current += c;
            } else if (c == ')') {
                current += c;
                if (--open == 0) {
                    result.push_back(current);
                    current = "";
                }
            }
        }
        if (open > 0) {
            result.push_back(current);
        }
        return result;
    }

D:
    vector<string> separate_paren_groups(string s) {
        vector<string> result;
        string current = "";
        int open = 0;

        for (char c : s) {
            if (c == '(') {
                open++;
                current += c;
            } else if (c == ')') {
                current += c;
                if (--open == 0) {
                    result.push_back(current);
                    current = "";
                }
            }
        }
        return result;
    }

E:
    vector<string> separate_paren_groups(string s) {
        vector<string> result;
        string current = "";
        int open = 0;

        for (char c : s) {
            if (c == '(') {
                open++;
                current += c;
            } else if (c ==