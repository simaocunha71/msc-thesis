    vector<string> all_words;
    vector<int> prime_words;
    int i;
    int j;
    int length;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]!=' ')
        all_words.push_back(sentence[i]);
    }
    for (i=0;i<all_words.size();i++)
    {
        length=all_words[i].length();
        for (j=2;j<length;j++)
        if (length%j==0)
        break;
        if (j==length)
        prime_words.push_back(length);
    }
    return "";
}
