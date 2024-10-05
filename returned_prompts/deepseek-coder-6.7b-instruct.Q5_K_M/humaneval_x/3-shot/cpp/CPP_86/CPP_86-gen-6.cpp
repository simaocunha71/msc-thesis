    int i, j, k;
    string words[50];
    string temp = "";
    string result = "";
    for(i = 0; i < s.length(); i++){
        if(s[i] == ' '){
            words[k] = temp;
            temp = "";
            k++;
        }
        else{
            temp += s[i];
        }
    }
    words[k] = temp;
    for(j = 0; j <= k; j++){
        sort(words[j].begin(), words[j].end());
        result += words[j];
        if(j != k){
            result += " ";
        }
    }
    return result;
}


