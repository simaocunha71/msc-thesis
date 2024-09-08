    int i = word.length() - 1;
    while(i >= 0 && !isvowel(word[i])) i--;
    if(i < 0) return "";
    int j = i - 1;
    while(j >= 0 && !isconsonant(word[j])) j--;
    if(j < 0) return "";
    return word.substr(j+1, i-j-1);
}

int isvowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

int isconsonant(char c) {
    return !isvowel(c);
}
B:
    string get_closest_vowel(string word) {
        int i = word.length() - 1;
        while (i >= 0 && !isvowel(word[i])) i--;
        if (i < 0) return "";
        int j = i - 1;
        while (j >= 0 && !isconsonant(word[j])) j--;
        if (j < 0) return "";
        return word.substr(j + 1, i - j - 1);
    }
    bool isvowel(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
    }
    bool isconsonant(char c) {
        return !isvowel(c);
    }
C:
    string get_closest_vowel(string word) {
        int i = word.length() - 1;
        while (i >= 0 && !isvowel(word[i])) i--;
        if (i < 0) return "";
        int j = i - 1;
        while (j >= 0 && !isconsonant(word[j])) j--;
        if (j < 0) return "";
        return word.substr(j + 1, i - j);
    }
    bool isvowel(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' ||