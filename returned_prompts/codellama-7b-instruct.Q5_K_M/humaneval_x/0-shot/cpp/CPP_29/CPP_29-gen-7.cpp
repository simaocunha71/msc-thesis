    vector<string> filtered;
    for (int i = 0; i < strings.size(); i++)
    {
        if (strings[i].compare(prefix) == 0)
        {
            filtered.push_back(strings[i]);
        }
    }
    return filtered;
}

