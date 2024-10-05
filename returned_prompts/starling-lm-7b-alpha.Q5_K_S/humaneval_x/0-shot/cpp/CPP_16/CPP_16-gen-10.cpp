    int res = 0;
    int len = str.length();
    for(int i = 0; i < len; i++) {
        int j = i;
        while(j < len && str[j] == str[i]) {
            j++;
        }
        if(j == len) {
            res++;
        }
    }
    return res;
}


B:
    int res = 0;
    for(int i = 0; i < str.length(); i++) {
        int j = i;
        while(j < str.length() && tolower(str[j]) == tolower(str[i])) {
            j++;
        }
        if(j == str.length()) {
            res++;
        }
    }
    return res;
}


C:
    int res = 0;
    sort(str.begin(), str.end());
    for(int i = 0; i < str.length() - 1; i++) {
        if(str[i] != str[i + 1]) {
            res++;
        }
    }
    return res + 1;
}


D:
    int res = 0;
    for(int i = 0; i < str.length(); i++) {
        int j = i;
        while(j < str.length() && str[j] != ' ' && str[j] != '\n' && str[j] != '\t') {
            j++;
        }
        if(j != str.length()) {
            res++;
        }
    }
    return res;
}


E:
    int res = 0;
    int len = str.length();
    for(int i = 0; i < len; i++) {
        int j = i;
        while(j < len && str[j] == str[i] && isdigit(str[j])) {
            j++;
        }
        if(j != len) {
            res++;
        }
    }
    return res;
}


F:
    int res = 0;
    for(int