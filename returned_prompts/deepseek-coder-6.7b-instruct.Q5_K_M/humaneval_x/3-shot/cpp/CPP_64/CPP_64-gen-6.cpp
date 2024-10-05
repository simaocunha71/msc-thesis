    string vowels="aeiou";
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    int count=0;
    for(char c:s){
        if(vowels.find(c)!=string::npos){
            count++;
        }
    }
    if(s[s.length()-1]=='y'){
        count++;
    }
    return count;
}


