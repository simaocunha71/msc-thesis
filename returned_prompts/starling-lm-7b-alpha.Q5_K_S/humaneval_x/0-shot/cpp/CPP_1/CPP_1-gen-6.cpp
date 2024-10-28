
Here's one way to do it:

```cpp
vector<string> separate_paren_groups(string paren_string) {
    vector<string> v;
    string cur;
    while (paren_string.size() > 0) {
        int open_pos = paren_string.find('(');
        int close_pos = paren_string.find(')');
        if (open_pos < 0 || close_pos < 0) break;
        if (open_pos < close_pos) {
            cur += '(';
            paren_string = paren_string.substr(open_pos + 1, paren_string.size() - (open_pos + 1)) + paren_string;
        } else {
            v.push_back(cur);
            cur = "";
            paren_string = paren_string.substr(0, close_pos) + paren