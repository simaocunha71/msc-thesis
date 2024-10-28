    vector<string> all_odds;
    map<int,string> all_words;
    string current_word;
    int level=0;
    char chr;
    int i;
    int j;
    int k;
    for (i=0;i<lst.size();i++)
    {
        int count=0;
        for (j=0;j<lst[i].length();j++)
        {
        chr=lst[i][j];
        if (chr%2==1)
        count+=1;
        }
        string current_word="the number of odd elements "+to_string(count)+"n the string "+to_string(i)+" of the input.";
        all_words[i]=current_word;
    }
    for (k=0;k<lst.size();k++)
    {
        all_odds.push_back(all_words[k]);
    }
    return all_odds;
}

