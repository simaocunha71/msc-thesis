    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'){
            count++;
        }else if(s[i] == 'y' && i == s.length() - 1){
            count++;
        }
    }
    return count;
}

B:
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || (s[i] == 'y' && i == s.length() - 1)){
            count++;
        }
    }
    return count;

C:
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if((s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') || (s[i] == 'y' && i == s.length() - 1)){
            count++;
        }
    }
    return count;

D:
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'y'){
            count++;
        }
    }
    return count;

E:
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || i == s.length() - 1 && s[i] == 'y'){
            count++;
        }
    }
    return count;

F:
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i]