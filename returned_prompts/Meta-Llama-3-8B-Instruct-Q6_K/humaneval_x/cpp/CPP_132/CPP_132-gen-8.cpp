    int stack = 0;
    for(int i = 0; i < str.length(); i++){
        if(str[i] == '[') stack++;
        else if(str[i] == ']') stack--;
        if(stack < 0) return true;
    }
    return false;
}

B:
    int count_open = 0;
    for(int i = 0; i < str.length(); i++){
        if(str[i] == '[') count_open++;
        else if(str[i] == ']'){
            count_open--;
            if(count_open < 0) return true;
        }
    }
    return false;
}

C:
    bool is_nested(string s){
        int count = 0;
        for(auto c : s){
            if(c == '[') count++;
            else if(c == ']') count--;
            if(count < 0) return true;
        }
        return false;
    }

D:
    bool is_nested(string s){
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '[') count++;
            else if(s[i] == ']') count--;
            if(count < 0) return true;
        }
        return false;
    }

E:
    bool is_nested(string s){
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '[') count++;
            else if(s[i] == ']') count--;
        }
        return count < 0;
    }

F:
    bool is_nested(string s){
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '[') count++;
            else if(s[i] == ']') count--;
            if(count < 0) return true;
        }
        return false;
    }

G:
    bool is_nested(string s){
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '[') count++;
            else if(s[i] == ']') count--;
            if(count < 0) return true;
        }
        return false;
    }

H:
    bool is_nested(string s){
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '[') count++;
            else if(s[i] == ']') count--;
