    string result;
    int n = s.length();
    for(int i = 0; i < n; i++) {
        if(s[i] >= 'a' && s[i] <= 'z') {
            result += (char)((s[i] - 'a' + 2 * 2) % 26 + 'a');
        } else if(s[i] >= 'A' && s[i] <= 'Z') {
            result += (char)((s[i] - 'A' + 2 * 2) % 26 + 'A');
        } else {
            result += s[i];
        }
    }
    return result;
}  // Your solution goes here
