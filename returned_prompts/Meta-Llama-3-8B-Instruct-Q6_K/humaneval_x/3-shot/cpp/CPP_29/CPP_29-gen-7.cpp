    vector<string> result;
    for (int i=0;i<strings.size();i++)
    {
        if (strings[i].find(prefix)==0)
        result.push_back(strings[i]);
    }
    return result;
} //This function is case sensitive. If you want a case insensitive filter, you can convert both strings to lower case and then compare. But this will make the function slower. 

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (int i=0;i<strings.size();i++)
    {
        if (strings[i].substr(0,prefix.size()).compare(prefix)==0)
        result.push_back(strings[i]);
    }
    return result;
} //This function is case sensitive. If you want a case insensitive filter, you can convert both strings to lower case and then compare. But this will make the function slower. 

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (int i=0;i<strings.size();i++)
    {
        if (toLower(strings[i].substr(0,prefix.size())).compare(toLower(prefix))==0)
        result.push_back(strings[i]);
    }
    return result;
} //This function is case insensitive. It converts both strings to lower case before comparing. It is slower than the previous two functions. 

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (int i=0;i<strings.size();i++)
    {
        if (strings[i].rfind(prefix)==0)
        result.push_back(strings[i]);
    }
    return result;
} //This function is case sensitive. It starts from the end of the string. If you want a case insensitive filter, you can convert both strings to lower case and then compare. But this will make the function slower. 

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (int i=0;i<strings.size();i++)
    {
        if (toLower(strings[i]).find(toLower(prefix))==0)
        result.push_back(strings[i]);
    }
    return result;
} //This function is case insensitive. It converts both strings to lower case before comparing. It is slower than the previous two functions. 

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    transform(prefix.begin(), prefix.end(), prefix.begin(), ::tolower