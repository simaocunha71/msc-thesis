    vector<string> result;
    for (string s : strings)
    {
        if (s.find(substring) != string::npos)
        {
            result.push_back(s);
        }
    }
    return result;
}