    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || (s[i] == 'y' && i == s.length()-1)){
            count++;
        }
    }
    return count;
}

B:
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'){
            count++;
        }
    }
    if(s.length() > 0 && s[s.length()-1] == 'y'){
        count++;
    }
    return count;
}

C:
    int count = 0;
    for(auto c : s){
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y'){
            count++;
        }
    }
    return count;
}
