    sort(words.begin(),words.end());
    int i,j,k;
    int max_count=0;
    string max_word;
    for (i=0;i<words.size();i++)
    {
        int count=0;
        for (j=0;j<words[i].length();j++)
        for (k=0;k<words[i].length();k++)
        if (words[i][j]==words[i][k])
        count+=1;
        if (count>max_count)
        {
        max_count=count;
        max_word=words[i];
        }
    }
    return max_word;
}


