    vector<string> words;
    string word;
    int i,j;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' '){
            if (isprime(word.length()))
            words.push_back(word);
            word="";
        }
        else
            word+=sentence[i];
    }
    if (isprime(word.length()))
        words.push_back(word);

    string result="";
    for (i=0;i<words.size();i++)
    result+=words[i];

    return result;
}



