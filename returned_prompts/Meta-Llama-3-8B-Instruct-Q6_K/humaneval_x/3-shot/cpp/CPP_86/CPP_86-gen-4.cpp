    string result;
    size_t start = 0;
    while (start < s.size()) {
        size_t end = start;
        while (end < s.size() && s[end] <= s[start]) {
            end++;
        }
        result += s.substr(start, end - start);
        start = end;
    }
    return result;
}