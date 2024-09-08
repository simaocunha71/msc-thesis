```cpp
vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    string current_group;
    int depth = 0;

    for (char c : paren_string) {
        if (c == '(') {
            if (depth == 0) {
                current_group = "";
            }
            depth++;
        } else if (c == ')') {
            depth--;
            if (depth == 0) {
                result.push_back(current_group);
            }
        } else if (depth > 0) {
            current_group += c;
        }
    }

    return result;
}
```

