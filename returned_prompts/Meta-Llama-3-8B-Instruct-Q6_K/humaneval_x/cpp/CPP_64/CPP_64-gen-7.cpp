    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
            count++;
        }
        else if(i == s.length() - 1 && s[i] == 'y'){
            count++;
        }
    }
    return count;
}

B:
    int count = 0;
    for (char c : s) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
        else if(s.length() - 1 == i && c == 'y'){
            count++;
        }
    }
    return count;
}

C:
    int count = 0;
    for (auto c : s) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
        else if(s.length() - 1 == distance(s.begin(), find(s.end(), c)) && c == 'y'){
            count++;
        }
    }
    return count;
}

D:
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
            count++;
        }
        else if(s.find('y') == s.length() - 1){
            count++;
        }
    }
    return count;

E:
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
            count++;
        }
        else if(i == s.length() - 1 && s[i] == 'y'){
            count++;
        }
    }
    return count;
}

F:
    int count = 0;
    for (auto c : s) {
        if (c == '