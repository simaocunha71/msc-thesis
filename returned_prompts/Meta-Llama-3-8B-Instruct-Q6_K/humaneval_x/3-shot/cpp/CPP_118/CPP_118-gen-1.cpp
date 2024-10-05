    string result;
    for(int i = word.length() - 1; i > 0; i--){
        if(isupper(word[i])){
            word[i] = tolower(word[i]);
        }
        if(isalpha(word[i]) && (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u')){
            return word.substr(i);
        }
    }
    return "";
}


