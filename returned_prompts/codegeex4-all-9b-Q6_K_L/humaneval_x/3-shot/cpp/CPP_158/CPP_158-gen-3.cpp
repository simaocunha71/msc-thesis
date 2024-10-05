    int max=0;
    string max_string="";
    int i;
    for (i=0;i<words.size();i++)
    {
        sort(words[i].begin(),words[i].end());
        words[i].erase(unique(words[i].begin(),words[i].end()),words[i].end());
        if (words[i].length()>max)
        {
            max=words[i].length();
            max_string=words[i];
        }
    }
    return max_string;
}