    vector<string> result;
    string word;
    for (char c : txt)
    {
        if (c == ' ' || c == ',')
        {
            if (!word.empty())
            {
                result.push_back(word);
                word.clear();
            }
        }
        else
        {
            word += c;
        }
    }
    if (!word.empty())
    {
        result.push_back(word);
    }
    else
    {
        int count = 0;
        for (char c : txt)
        {
            if (islower(c))
            {
                count++;
            }
        }
        result.push_back(to_string(count));
    }
    return result;
}