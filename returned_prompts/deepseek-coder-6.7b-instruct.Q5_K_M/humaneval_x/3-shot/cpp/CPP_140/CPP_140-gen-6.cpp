    string res;
    int cnt = 0;
    for(char c : text){
        if(c == ' '){
            cnt++;
            if(cnt == 2){
                res += '-';
            }
        }
        else{
            if(cnt >= 2){
                res += '_';
            }
            res += c;
            cnt = 0;
        }
    }
    return res;
}

