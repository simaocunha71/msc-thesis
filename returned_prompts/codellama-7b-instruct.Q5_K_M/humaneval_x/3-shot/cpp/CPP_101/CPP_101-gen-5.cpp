    vector<string> words;
    int i=0;
    while (i<s.length())
    {
        if (s[i]==',')
        {
            words.push_back(s.substr(i+1,s.find(",",i)-i-1));
            i=s.find(",",i)+1;
        }
        else
        {
            words.push_back(s.substr(i,s.find(" ",i)-i));
            i=s.find(" ",i)+1;
        }
    }
    return words;
}


