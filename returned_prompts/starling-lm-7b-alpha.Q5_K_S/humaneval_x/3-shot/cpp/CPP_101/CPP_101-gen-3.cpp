    vector<string> words;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if ((chr==' ')||(chr==','))
        {
            words.push_back(" ");
        }
        else
        {
            if (i==0){
            words.push_back("");
            }
            words[words.size()-1]+=chr;
        }
    }
    return words;
}


