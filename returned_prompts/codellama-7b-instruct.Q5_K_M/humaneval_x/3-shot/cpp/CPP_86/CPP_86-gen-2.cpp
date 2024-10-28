    stringstream ss(s);
    string word;
    vector<string> words;
    while (ss>>word)
    words.push_back(word);
    sort(words.begin(),words.end());
    string res="";
    for (int i=0;i<words.size();i++)
    {
        res+=words[i];
        res+=" ";
    }
    return res.substr(0,res.length()-1);
}



