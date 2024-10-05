    vector<string> words;
    int i;
    if (txt.find(' ')!=string::npos){
        for (i=0;i<txt.length();i++)
        if (txt[i]==' ')
        words.push_back(txt.substr(0,i));
        txt=txt.substr(i+1,txt.length());
        goto A;
    }
    if (txt.find(',')!=string::npos){
        for (i=0;i<txt.length();i++)
        if (txt[i]==',')
        words.push_back(txt.substr(0,i));
        txt=txt.substr(i+1,txt.length());
        goto A;
    }
    stringstream ss;
    int count=0;
    for (i=0;i<26;i++)
    if (islower(i)){
        if (i%2==0)
        count++;
    }
    words.push_back(to_string(count));
    return words;
}


