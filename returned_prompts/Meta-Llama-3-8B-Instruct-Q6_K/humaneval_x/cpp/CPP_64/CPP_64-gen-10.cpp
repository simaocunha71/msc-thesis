    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        char ch = tolower(s[i]);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            count++;
        }
        else if (ch == 'y' && i == s.length() - 1) {
            count++;
        }
    }
    return count;
}

B:
    int vowels_count(string s){
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'y' && i == s.length() - 1) {
                count++;
            }
        }
        return count;
}

C:
    int vowels_count(string s){
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (tolower(s[i]) == 'a' || tolower(s[i]) == 'e' || tolower(s[i]) == 'i' || tolower(s[i]) == 'o' || tolower(s[i]) == 'u') {
                count++;
            }
        }
        return count;
}

D:
    int vowels_count(string s){
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isalpha(s[i]) && (tolower(s[i]) == 'a' || tolower(s[i]) == 'e' || tolower(s[i]) == 'i' || tolower(s[i]) == 'o' || tolower(s[i]) == 'u')) {
                count++;
            }
        }
        if (isalpha(s[s.length() - 1]) && tolower(s[s.length() - 1]) == 'y') {
            count++;
        }
        return count;
}

E:
    int vowels_count(string s){
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isalpha(s[i]) && (tolower(s[i]) == 'a' || tolower(s[i]) == 'e' || tolower(s[i]) ==