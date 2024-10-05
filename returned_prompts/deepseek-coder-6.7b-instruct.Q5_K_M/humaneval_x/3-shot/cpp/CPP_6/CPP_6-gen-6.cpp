    vector<int> results;
    string group;
    string::size_type start = 0;
    string::size_type end = 0;

    while(end != string::npos)
    {
        end = paren_string.find(' ', start);
        group = paren_string.substr(start, end - start);
        start = end != string::npos ? end + 1 : string::npos;

        int level = 0;
        int max_level = 0;
        for(char c : group)
        {
            if(c == '(')
            {
                level++;
                if(level > max_level)
                {
                    max_level = level;
                }
            }
            else if(c == ')')
            {
                level--;
            }
        }

        results.push_back(max_level);
    }

    return results;
}

