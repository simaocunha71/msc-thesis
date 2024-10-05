    int count = 0;
    string vowels = "aeiou";
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    for(int i = 0; i < s.size(); i++){
        if(vowels.find(s[i]) != string::npos){
            count++;
        }
    }
    if(s[s.size()-1] == 'y'){
        count++;
    }
    return count;
}


