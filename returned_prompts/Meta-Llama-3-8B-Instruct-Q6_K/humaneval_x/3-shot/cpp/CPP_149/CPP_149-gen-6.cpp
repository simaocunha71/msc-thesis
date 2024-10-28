    vector<string> result;
    for (vector<string>::iterator it = lst.begin(); it != lst.end(); ++it)
    {
        if (it->length() % 2 == 0)
        {
            result.push_back(*it);
        }
    }
    sort(result.begin(), result.end(), [](string a, string b)
    {
        if