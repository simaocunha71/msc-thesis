    vector<string> words;
    string current_word;
    bool is_comma = false;
    
    for (char chr : txt)
    {
        if (chr == ' ')
        {
            if (!current_word.empty())
            {
                words.push_back(current_word);
                current_word.clear();
            }
        }
        else if (chr == ',')
        {
            is_comma = true;
        }
        else
        {
            if (is_comma)
            {
                current_word += chr;
                is_comma = false;
            }
            else
            {
                current_word += chr;
            }
        }
    }
    
    if (!current_word.empty())
    {
        words.push_back(current_word);
    }
    else if (txt.empty())
    {
        int count = 0;
        for (char chr : txt)
        {
            if (chr >= 'a' && chr <= 'z' && (chr-'a')%2 != 0)
            {
                count++;
            }
        }
        words.push_back(to_string(count));
    }
    
    return words;
}