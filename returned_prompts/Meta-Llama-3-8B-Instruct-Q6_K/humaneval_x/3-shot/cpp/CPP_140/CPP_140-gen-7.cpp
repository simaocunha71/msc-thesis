    string result;
    for(int i=0; i<text.length(); i++){
        if(result.length() && result[result.length()-1] == ' '){
            if(i < text.length() - 1 && text[i+1] == ' '){
                result += '-';
            }
            else{
                result += '_';
            }
        }
        else{
            result += text[i] == ' ' ? '_' : text[i];
        }
    }
    return result;
}