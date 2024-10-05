    string vowels="AEIOUaeiou";
    char c;
    for(int i=word.size()-2;i>0;i--){
        c=word[i];
        if(vowels.find(c)!=string::npos && 
        !(vowels.find(word[i-1])==string::npos && vowels.find(word[i+1])==string::npos))
        return string(1,c);
    }
    return "";
}


