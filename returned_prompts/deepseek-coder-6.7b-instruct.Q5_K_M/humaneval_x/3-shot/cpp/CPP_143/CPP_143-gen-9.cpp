    string words[50];
    string res="";
    int i,j,k=0,len=0,flag;
    for(i=0;sentence[i] != '\0';i++){
        if(sentence[i] == ' '){
            words[k++] = sentence.substr(len,i-len);
            len = i+1;
        }
    }
    words[k++] = sentence.substr(len,i-len);
    for(j=0;j<k;j++){
        if(words[j].length()<=1){
            continue;
        }
        flag = 0;
        for(i=2;i*i<=words[j].length();i++){
            if(words[j].length() % i == 0){
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            if(res == ""){
                res += words[j];
            }
            else{
                res += " " + words[j];
            }
        }
    }
    return res;
}


