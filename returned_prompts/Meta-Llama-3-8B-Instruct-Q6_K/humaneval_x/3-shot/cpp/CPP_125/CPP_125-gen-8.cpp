    vector<string> words;
    string word;
    for (char chr : txt)
    {
        if (chr == ' ' || chr == ',')
        {
            if (!word.empty())
            {
                words.push_back(word);
                word.clear();
            }
        }
        else
        {
            word += chr;
        }
    }
    if (!word.empty())
    {
        words.push_back(word);
    }
    else
    {
        int count = 0;
        for (char c : txt)
        {
            if (islower(c))
            {
                if ((int)c - 97 % 2 != 0)
                {
                    count++;
                }
            }
        }
        words.push_back(to_string(count));
    }
    return words;
}