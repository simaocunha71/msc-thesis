    // replace all spaces with underscores
    for(int i=0;i<text.length();i++){
        if(text[i] == ' '){
            text[i] = '_';
        }
    }
    // replace all consecutive spaces with -
    int j=0;
    while(j<text.length()){
        if(text[j] == ' '){
            j++;
            while(j<text.length() && text[j] == ' '){
                j++;
            }
            text.insert(j,'-');
        }else{
            j++;
        }
    }
    return text;
}

B:
    // replace all spaces with underscores
    string res = "";
    for(int i=0;i<text.length();i++){
        if(text[i] == ' '){
            res += "_";
        }else{
            res += text[i];
        }
    }
    // replace all consecutive spaces with -
    res = res + "-";
    for(int i=res.length()-1;i>0;--i){
        if(res[i-1] == '_' && res[i] == '_'){
            res = res.substr(0,i-1) + "-" + res.substr(i);
        }
    }
    return res;
}

C:
    // replace all spaces with underscores
    string res = "";
    for(int i=0;i<text.length();i++){
        if(text[i] == ' '){
            res += "_";
        }else{
            res += text[i];
        }
    }
    // replace all consecutive spaces with -
    int cnt = 0;
    for(int i=0;i<res.length();i++){
        if(res[i] == '_'){
            cnt++;
        }else{
            if(cnt > 1){
                res.insert(i,"-");
                cnt = 1;
            }
        }
    }
    return res;
}

D:
    // replace all spaces with underscores
    string res = "";
    for(int i=0;i<text.length();i++){
        if(text[i] == ' '){
            res += "_";
        }else{
            res += text[i];
        }
    }
    // replace all consecutive spaces with -
    int start = 0;
    for(int i=0;i<res.length();i++){
        if(res[i] == '_'){
            if(start < i){
                res.insert(start,"-");
                start = i + 1;
            }
        }else{
            start = i + 1;
        }
    }
    return res;
}

int