    string s = to_string(x);
    int n = s.length();
    shift = shift % n;
    if(shift == 0) return s;
    string res = s.substr(shift) + s.substr(0,shift);
    return res;

}  // Correct
B:
    string s = to_string(x);
    int n = s.length();
    shift = shift % n;
    if(shift == 0) return s;
    int start = 0;
    int end = n - 1;
    while(shift--){
        start++;
        end--;
    }
    return s.substr(start) + s.substr(0,start) + s.substr(end+1,n-end-1);

}  // Wrong

C:
    string s = to_string(x);
    int n = s.length();
    shift = shift % n;
    if(shift == 0) return s;
    string res = "";
    for(int i = shift; i < n; i++){
        res += s[i];
    }
    for(int i = 0; i < shift; i++){
        res += s[i];
    }
    return res;

}  // Wrong

D:
    string s = to_string(x);
    int n = s.length();
    shift = shift % n;
    if(shift == 0) return s;
    string res = "";
    for(int i = shift; i < n; i++){
        res += s[i];
    }
    for(int i = 0; i < shift; i++){
        res += s[i];
    }
    return res;

}  // Wrong

E:
    string s = to_string(x);
    int n = s.length();
    shift = shift % n;
    if(shift == 0) return s;
    string res = "";
    for(int i = 0; i < n - shift; i++){
        res += s[i];
    }
    for(int i = n - shift; i < n; i++){
        res += s[i];
    }
    return res;

}  // Wrong

F:
    string s = to_string(x);
    int n = s.length();
    shift = shift % n;
    if(shift == 0) return s;
    string res = "";
    int start = 0;
    int end = n - 1;
    while(shift--){
        start++;
        end--;
    }
    res += s.substr(start) + s.substr(0,start) + s.substr(end+1