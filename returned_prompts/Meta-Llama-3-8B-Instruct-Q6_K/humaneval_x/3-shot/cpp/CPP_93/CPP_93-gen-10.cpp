    string result = "";
    for (char c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            c = (c - base + (isupper(c) ? 2 : 0)) % 26 + base;
            if (c == ' ') {
                result += ' ';
            } else {
                result += c;
            }
        } else {
            result += c;
        }
    }
    return result;
}
```
