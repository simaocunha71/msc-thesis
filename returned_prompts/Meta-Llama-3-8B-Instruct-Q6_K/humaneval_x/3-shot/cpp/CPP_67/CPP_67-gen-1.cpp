    int mangoes = n;
    int i = 0;
    while(i<s.length()){
        if(s[i] == 'o' && s[i+1] == 'r' && s[i+2] == 'a' && s[i+3] == 'n' && s[i+4] == 'g' && s[i+5] == 'e' && s[i+6] == 's'){
            istringstream iss(s.substr(i+7));
            string temp;
            getline(iss,temp,' ');
            mangoes -= stol(temp.substr(0,temp.find(' ')));
            getline(iss,temp,' ');
            mangoes -= stol(temp.substr(0,temp.find(' ')));
            i += s.find_last_of('s')+6;
        }
        i++;
    }
    return mangoes;
}
```

