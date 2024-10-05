    int i = 0, count = 0;
    while(i < S.length()){
        if(S[i] == 'I'){
            while(S[i] != '.' && S[i] != '!' && S[i] != '?'){
                i++;
            }
            count++;
        }
        i++;
    }
    return count;
}


