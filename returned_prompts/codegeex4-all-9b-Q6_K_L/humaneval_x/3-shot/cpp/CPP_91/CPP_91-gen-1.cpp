    int i=0;
    int count=0;
    while (i<S.length()){
        char chr=S[i];
        if (chr=='I'){
            while (i<S.length()){
                char chr=S[i];
                if (chr=='.'||chr=='?'||chr=='!'){
                    count+=1;
                    break;
                }
                i+=1;
            }
        }
        i+=1;
    }
    return count;
}

