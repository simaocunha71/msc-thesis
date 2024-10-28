    vector<string> words;
    string current_word;
    for (char chr:txt)
    {
        if (chr == ' ' || chr == ',')
        {
            if (!current_word.empty())
            {
                words.push_back(current_word);
                current_word.clear();
            }
        }
        else
        {
            current_word += chr;
        }
    }
    if (!current_word.empty())
    {
        words.push_back(current_word);
    }
    else
    {
        int count=0;
        for (char chr:txt)
        {
            if (chr >= 'a' && chr <= 'z' && (int)chr - 'a' % 2 == 1)
                count++;
        }
        words.push_back(to_string(count));
    }
    return words;
}