    vector<string> words;
    string word;
    int i,j,counter;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' '){
            if (counter==n){
                words.push_back(word);
            }
            counter=0;
            word="";
        }
        else
        {
            word+=s[i];
            if (s[i]!='a' && s[i]!='e' && s[i]!='i' && s[i]!='o' && s[i]!='u')
            counter+=1;
        }
    }
    return words;
}

