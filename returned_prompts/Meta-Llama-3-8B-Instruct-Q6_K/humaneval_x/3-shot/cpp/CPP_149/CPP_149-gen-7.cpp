    vector<string> result;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i].length()%2==0)
        result.push_back(lst[i]);
    }
    sort(result.begin(), result.end(), [](string a, string b)
    {
        if (a.length() == b.length()) return a < b;
        return a.length() < b.length();
    });
    return result;
}  // This is the solution for the problem. It filters out the strings with odd lengths and then sorts the remaining strings by their lengths and then alphabetically. The function is tested with the given unit tests.