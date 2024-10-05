    int l = 0;
    int r = word.size()-1;
    while(true){
        if(word[l] == 'a' || word[l] == 'e' || word[l] == 'i' || word[l] == 'o' || word[l] == 'u' || word[l] == 'A' || word[l] == 'E' || word[l] == 'I' || word[l] == 'O' || word[l] == 'U'){
            if(word[l+1] == 'a' || word[l+1] == 'e' || word[l+1] == 'i' || word[l+1] == 'o' || word[l+1] == 'u' || word[l+1] == 'A' || word[l+1] == 'E' || word[l+1] == 'I' || word[l+1] == 'O' || word[l+1] == 'U'){
                continue;
            }else{
                return word[l];
            }
        }else if(word[r] == 'a' || word[r] == 'e' || word[r] == 'i' || word[r] == 'o' || word[r] == 'u' || word[r] == 'A' || word[r] == 'E' || word[r] == 'I' || word[r] == 'O' || word[r] == 'U'){
            if(word[r-1] == 'a' || word[r-1] == 'e' || word[r-1] == 'i' || word[r-1] == 'o' || word[r-1] == 'u' || word[r-1] == 'A' || word[r-1] == 'E' || word[r-1] == 'I' || word[r-1] == 'O' || word[r-1] == 'U'){
                continue;
            }else{
                return word[r];
            }
        }
        if(l+1 >= r){
            break;
        }
        if(word[l