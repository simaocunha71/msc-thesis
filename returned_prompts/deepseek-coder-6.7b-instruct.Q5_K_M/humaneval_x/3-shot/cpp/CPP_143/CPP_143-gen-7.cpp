    string words[50];
    int i=0, j, count=0, k, l, flag;
    string word="", result="";
    while(sentence[i]){
        if(sentence[i] != ' '){
            word += sentence[i];
        }
        else{
            words[count] = word;
            count++;
            word = "";
        }
        i++;
    }
    words[count] = word; //to store the last word
    count++;

    for(i=0; i<count; i++){
        flag = 0;
        if(words[i].length() <= 1){
            continue;
        }
        for(j=2; j<=words[i].length()/2; j++){
            if(words[i].length() % j == 0){
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            if(result.length() != 0){
                result += " ";
            }
            result += words[i];
        }
    }
    return result;
}

