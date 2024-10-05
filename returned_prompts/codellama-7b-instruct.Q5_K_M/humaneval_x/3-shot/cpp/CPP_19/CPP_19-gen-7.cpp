    map<string,int> m;
    m["zero"]=0;
    m["one"]=1;
    m["two"]=2;
    m["three"]=3;
    m["four"]=4;
    m["five"]=5;
    m["six"]=6;
    m["seven"]=7;
    m["eight"]=8;
    m["nine"]=9;

    stringstream ss(numbers);
    string word;
    vector<string> words;
    while (ss>>word)
    {
        words.push_back(word);
    }

    sort(words.begin(),words.end(),[&m](string a, string b){
        return m[a]<m[b];
    });

    return words[0]+" "+words[1]+" "+words[2];
}



