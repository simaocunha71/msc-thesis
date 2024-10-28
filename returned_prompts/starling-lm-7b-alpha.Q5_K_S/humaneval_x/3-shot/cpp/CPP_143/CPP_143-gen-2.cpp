    vector<string> words;
    int i,j;
    char chr;
    for (i=0;i<sentence.length();i++)
    {
        chr=sentence[i];
        if (chr==' '){
            words.push_back("" + sentence.substr(i-1,1));
        }
        if (chr!=' '){
            words.push_back("" + sentence.substr(i,1));
        }
    }

    for (i=0;i<words.size();i++)
    {
        if (words[i].length()==2 && words[i]=="is")
        {
            words.erase(words.begin()+i);
            return "is";
        }
        if (words[i].length()==3 && words[i]=="the")
        {
            words.erase(words.begin()+i);
            return "the";
        }
    }
    vector<int> lengths;
    for (i=0;i<words.size();i++)
    {
        lengths.push_back(words[i].length());
    }
    for (i=0;i<lengths.size();i++)
    {
        if (lengths[i]==2 && is_prime(lengths[i]))
        {
            return words[i];
        }
        if (lengths[i]==3 && is_prime(lengths[i]))
        {
            return words[i];
        }
    }
    return "";
}



