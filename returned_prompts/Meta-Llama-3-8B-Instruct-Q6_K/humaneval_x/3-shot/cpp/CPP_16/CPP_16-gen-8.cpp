    vector<char> chars;
    for (int i=0; i<str.length(); i++) {
        chars.push_back(tolower(str[i]));
    }
    sort(chars.begin(), chars.end());
    int count = 0;
    for (int i=0; i<chars.size(); i++) {
        if (chars[i] != chars[i+1]) {
            count++;
        }
    }
    return count+1; // +1 for the first character
} 


