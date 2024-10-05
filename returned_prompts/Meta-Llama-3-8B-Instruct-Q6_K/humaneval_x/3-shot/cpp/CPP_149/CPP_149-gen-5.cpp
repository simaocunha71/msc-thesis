    vector<string> result;
    for (vector<string>::iterator it = lst.begin(); it != lst.end(); ++it)
    {
        if (it->length() % 2 == 0)
        {
            result.push_back(*it);
        }
    }
    sort(result.begin(), result.end(), [](const string& a, const string& b) {
        if (a.length() == b.length())
            return a < b;
        return a.length() < b.length();
    });
    return result;
}  // This function is not perfect, as it doesn't remove duplicate strings.  // It will return a vector of strings in sorted order.