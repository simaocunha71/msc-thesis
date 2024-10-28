    vector<string> all_words;
    vector<string> max_words;
    int i;
    for (i=0;i<words.size();i++)
    {
        string current_word=words[i];
        int j;
        for (j=0;j<current_word.length();j++)
        {
            bool already_exists=false;
            for (int k=0;k<all_words.size();k++)
            if (all_words[k]==current_word[j])
                already_exists=true;

            if (!already_exists)
                all_words.push_back(current_word[j]);
        }
    }

    sort(all_words.begin(),all_words.end());
    all_words.erase(unique(all_words.begin(),all_words.end()),all_words.end());

    for (i=0;i<words.size();i++)
    {
        string current_word=words[i];
        int j;
        int k;
        for (j=0;j<current_word.length();j++)
        {
            for (k=0;k<all_words.size();k++)
            if (current_word[j]==all_words[k])
                break;

            if (k==all_words.size())
                max_words.push_back(current_word);
        }
    }

    if (max_words.size()==0)
        return words[0];

    sort(max_words.begin(),max_words.end());
    return max_words[0];
}


















































































































