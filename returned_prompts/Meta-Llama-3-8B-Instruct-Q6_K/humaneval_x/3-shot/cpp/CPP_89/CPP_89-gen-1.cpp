    string result = "";
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if (c >= 'a' && c <= 'z') {
            c = (c - 'a' + 26) % 26 + 'a';
        } else if (c >= 'A' && c <= 'Z') {
            c = (c - 'A' + 26) % 26 + 'A';
        }
        result += c;
    }
    return result;
}