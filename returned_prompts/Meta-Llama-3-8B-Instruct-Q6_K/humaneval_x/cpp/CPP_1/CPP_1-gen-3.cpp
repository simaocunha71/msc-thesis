    vector<string> result;
    string current_group = "";
    bool in_group = false;

    for (char c : paren_string) {
        if (c == '(') {
            if (!in_group) {
                in_group = true;
                current_group += c;
            } else {
                current_group += c;
            }
        } else if (c == ')') {
            if (in_group) {
                current_group += c;
                if (current_group.length() > 1 && current_group.back() == '(') {
                    current_group.pop_back();
                }
                result.push_back(current_group);
                current_group = "";
                in_group = false;
            }
        } else {
            if (in_group) {
                current_group += c;
            }
        }
    }

    return result;
}

