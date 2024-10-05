    int count = 0;
    for(int i=0;i<S.size();i++){
        if(S[i]=='.'||S[i]=='!'||S[i]=='?'){
            if(S[i-1]=='I'){
                count++;
            }
        }
    }
    return count;
}