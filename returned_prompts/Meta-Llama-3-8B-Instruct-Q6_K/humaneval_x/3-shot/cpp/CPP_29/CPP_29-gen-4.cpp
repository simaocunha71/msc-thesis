    vector<string> result;
    for (auto &s : strings)
    {
        if (s.find(prefix)==0)
            result.push_back(s);
    }
    return result;
}
// Alternative solution
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (auto &s : strings)
    {
        if (s.size()>=prefix.size() && s.substr(0, prefix.size())==prefix)
            result.push_back(s);
    }
    return result;
} 

