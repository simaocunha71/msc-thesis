    int i = 0;
    int j = word.size()-1;
    while(i<j){
        if(word[i]=='A' || word[i]=='E' || word[i]=='I' || word[i]=='O' || word[i]=='U'){
            if(word[j]=='A' || word[j]=='E' || word[j]=='I' || word[j]=='O' || word[j]=='U'){
                return "";
            }
            return string(1, word[i]);
        }
        i++;
        j--;
    }
    return "";
}


