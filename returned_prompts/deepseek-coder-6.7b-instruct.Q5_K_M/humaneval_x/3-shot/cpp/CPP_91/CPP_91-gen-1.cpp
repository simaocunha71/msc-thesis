    int i=0,count=0;
    string word;
    stringstream ss(S);
    while(ss >> word){
        if(word[0] == 'I')
            count++;
        if(word[word.size()-1] == '.' || word[word.size()-1] == '!' || word[word.size()-1] == '?')
            i++;
    }
    if(i>0)
        count++;
    return count;
}

