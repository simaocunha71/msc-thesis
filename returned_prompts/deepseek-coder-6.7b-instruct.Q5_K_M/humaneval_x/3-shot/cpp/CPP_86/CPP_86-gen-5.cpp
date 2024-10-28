    string word="";
    for(char c : s)
        if(c != ' ')
            word+=c;
    sort(word.begin(), word.end());
    int j=0;
    for(int i=0;i<s.length();i++)
        if(s[i] != ' ')
            s[i]=word[j++];
    return s;
}

