    int n = s.length();
    for(int i = 0; i < n; i++){
        s[i] = (char)(s[i] + 2*2);
        if(s[i] > 'z'){
            s[i] = (char)(s[i] - 26);
        }
    }
    return s;
}

B:
    int n = s.length();
    for(int i = 0; i < n; i++){
        if(s[i] >= 'a' && s[i] <= 'z'){
            s[i] = (char)((s[i] - 'a' + 2*2) % 26 + 'a');
        } else if(s[i] >= 'A' && s[i] <= 'Z'){
            s[i] = (char)((s[i] - 'A' + 2*2) % 26 + 'A');
        }
    }
    return s;
}

C:
    int n = s.length();
    for(int i = 0; i < n; i++){
        if(s[i] >= 'a' && s[i] <= 'z'){
            s[i] = (char)((s[i] - 'a' + 26 + 2*2) % 26 + 'a');
        } else if(s[i] >= 'A' && s[i] <= 'Z'){
            s[i] = (char)((s[i] - 'A' + 26 + 2*2) % 26 + 'A');
        }
    }
    return s;

D:
    int n = s.length();
    for(int i = 0; i < n; i++){
        if(s[i] >= 'a' && s[i] <= 'z'){
            s[i] = (char)((s[i] - 'a' + 2*2) % 26 + 'a');
        } else if(s[i] >= 'A' && s[i] <= 'Z'){
            s[i] = (char)((s[i] - 'A' + 2*2) % 26 + 'A');
        }
    }
    return s;

E:
    int n = s.length();
    for(int i = 0; i < n; i++){
        if(s[i] >= 'a' && s[i] <= 'z'){
            s[i] = (char)((s[i] - 'a' + 2*2) % 26 +