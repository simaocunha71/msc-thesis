    vector<string> all_parens;
    string current_paren;
    int depth = 0;
    char chr;
    for (int i = 0; i < paren_string.length(); i++) {
        chr = paren_string[i];
        if (chr == '(') {
            depth++;
            current_paren += chr;
        } else if (chr == ')') {
            depth--;
            current_paren += chr;
            if (depth == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;

The third question is also a bit overcomplicated. You don't need to use math