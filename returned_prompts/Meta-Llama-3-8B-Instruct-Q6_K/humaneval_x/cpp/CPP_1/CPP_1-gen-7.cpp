    vector<string> result;
    int open_count = 0;
    string current_group = "";
    for (int i = 0; i < paren_string.size(); i++) {
        if (paren_string[i] == '(') {
            open_count++;
            current_group += paren_string[i];
        } else if (paren_string[i] == ')') {
            open_count--;
            current_group += paren_string[i];
            if (open_count == 0) {
                result.push_back(current_group);
                current_group = "";
            }
        }
    }
    return result;
}

B:
    vector<string> separate_paren_groups(string paren_string) {
        vector<string> result;
        string current_group = "";
        int open_count = 0;
        for (char c : paren_string) {
            if (c == '(') {
                open_count++;
                current_group += c;
            } else if (c == ')') {
                open_count--;
                current_group += c;
                if (open_count == 0) {
                    result.push_back(current_group);
                    current_group = "";
                }
            }
        }
        return result;
    }

C:
    vector<string> separate_paren_groups(string paren_string) {
        vector<string> result;
        string current_group = "";
        int open_count = 0;
        for (int i = 0; i < paren_string.size(); i++) {
            if (paren_string[i] == '(') {
                open_count++;
                current_group += '(';
            } else if (paren_string[i] == ')') {
                open_count--;
                current_group += ')';
                if (open_count == 0) {
                    result.push_back(current_group);
                    current_group = "";
                }
            }
        }
        return result;
    }

D:
    vector<string> separate_paren_groups(string paren_string) {
        vector<string> result;
        string current_group = "";
        int open_count = 0;
        for (int i = 0; i < paren_string.size(); i++) {
            if (paren_string[i] == '(') {
                open_count++;
                current_group += '(';
            } else if (paren_string[i] == ')') {
                open_count--;
                current_group += ')';
                if (open_count == 0) {
                    result.push_back(current_group);
                    current_group = "";
                }
            }
        }
        return result;
    }

E:
    vector<string> separate_paren_groups(string paren_string) {
       