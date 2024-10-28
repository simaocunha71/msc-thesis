    vector<int> count(128,0);
    string max_word;
    int max_count=0;
    int i,j;
    for (i=0;i<words.size();i++)
    {
        for (j=0;j<words[i].length();j++)
        count[words[i][j]]+=1;
    }
    for (i=0;i<words.size();i++)
    {
        if (count[words[i][0]]>max_count)
        {
            max_count=count[words[i][0]];
            max_word=words[i];
        }
    }
    sort(max_word.begin(),max_word.end());
    return max_word;
}



