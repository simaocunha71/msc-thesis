    vector<string> all_words;
    string word;
    int count=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (chr==' '){
            if (count==n){
                all_words.push_back(word);
            }
            word="";
            count=0;
        }
        else if (isalpha(chr)){
            if (!isupper(chr))
                count+=1;
            word+=chr;
        }
    }
    if (count==n)
        all_words.push_back(word);
    sort(all_words.begin(),all_words.end());
    return all_words;
}


