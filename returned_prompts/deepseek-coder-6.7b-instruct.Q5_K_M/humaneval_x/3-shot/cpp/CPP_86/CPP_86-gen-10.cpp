    string word="";
    for(auto x:s)
    {
        if(x==' ')
        {
            sort(word.begin(), word.end());
            s.replace(s.find(word), word.length(), word);
            word="";
        }
        else
        word+=x;
    }
    sort(word.begin(), word.end());
    s.replace(s.find(word), word.length(), word);
    return s;
}


