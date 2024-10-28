    int apple_count=0,orange_count=0;
    int i=0;
    string temp="";
    while(s[i] != ' '){
        temp += s[i];
        i++;
    }
    apple_count = stoi(temp);
    temp="";
    i+=4;
    while(i<s.length()){
        temp+=s[i];
        i++;
    }
    orange_count = stoi(temp);
    return n-apple_count-orange_count;
}


