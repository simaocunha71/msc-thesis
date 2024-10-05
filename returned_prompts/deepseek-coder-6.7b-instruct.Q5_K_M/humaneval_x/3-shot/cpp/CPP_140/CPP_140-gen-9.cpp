    string result = "";
    int i = 0;
    while(i < text.length()){
        if(text[i] == ' ' && text[i+1] == ' '){
            result += "-";
            while(text[i] == ' ' && text[i+1] == ' ') i++;
        }
        else if(text[i] == ' '){
            result += "_";
        }
        else{
            result += text[i];
        }
        i++;
    }
    return result;
}

