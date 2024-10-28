    vector<string> words;
    int i=0;
    int j=0;
    int comma_pos;
    string word;
    while (i<txt.length())
    {
        j=i;
        while (txt[j]!=' '&&txt[j]!=',')
        j+=1;
        word=txt.substr(i,j-i);
        i=j+1;
        words.push_back(word);
    }
    return words;
}



