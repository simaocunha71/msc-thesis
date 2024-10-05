    string max_word;
    int max_count=0;
    for (auto word : words)
    {
        int count = word.length();
        set<char> s(word.begin(), word.end());
        count = s.size();
        if (count > max_count || (count == max_count && word < max_word))
        {
            max_word = word;
            max_count = count;
        }
    }
    return max_word;
}