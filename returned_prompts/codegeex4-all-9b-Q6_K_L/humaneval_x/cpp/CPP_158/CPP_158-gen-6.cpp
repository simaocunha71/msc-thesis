```cpp
string maxStr;
int maxUnique = 0;
for (string word : words) {
    int unique = 0;
    vector<bool> charSet(26, false);
    for (char c : word) {
        if (!charSet[c - 'a']) {
            unique++;
            charSet[c - 'a'] = true;
        }
    }
    if (unique > maxUnique) {
        maxUnique = unique;
        maxStr = word;
    } else if (unique == maxUnique) {
        maxStr = min(maxStr, word);
    }
}
return maxStr;
}
```

B:
```cpp
string find_max(vector<string> words){
    string maxStr;
    int maxUnique = 0;
    for (string word : words) {
        int unique = 0;
        vector<bool> charSet(26, false);
        for (char c : word) {
            if (!charSet[c - 'a']) {
                unique++;
                charSet[c - 'a'] = true;
            }
        }
        if (unique > maxUnique) {
            maxUnique = unique;
            maxStr = word;
        }
        else if (unique == maxUnique && word < maxStr) {
            maxStr = word;
        }
    }
    return maxStr;
}
```

C:
```cpp
string find_max(vector<string> words){
    string maxStr;
    int maxUnique = 0;
    for (string word : words) {
        int unique = 0;
        vector<bool> charSet(26, false);
        for (char c : word) {
            if (!charSet[c - 'a']) {
                unique++;
                charSet[c - 'a'] = true;
            }
        }
        if (unique > maxUnique) {
            maxUnique = unique;
            maxStr = word;
        } else if (unique == maxUnique) {
            maxStr = min(maxStr, word);
        }
    }
    return maxStr;
}
```

D:
```cpp
string find_max(vector<string> words){
    string maxStr;
    int maxUnique = 0;
    for (string word : words) {
        int unique = 0;
        vector<bool> charSet(26, false);
        for (char c : word) {
            if (!charSet[c - 'a']) {
                unique++;
                charSet[c - 'a'] = true;
            }
       