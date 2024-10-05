    int count=0;
    string vowels = "aeiou";
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    for(int i=0; i<s.length(); i++){
        if(vowels.find(s[i]) != std::string::npos)
            count++;
    }
    if(s[s.length()-1] == 'y')
        count++;
    return count;
}

