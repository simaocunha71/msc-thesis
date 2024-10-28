    if (strings.size()==0)
    return "";
    string longest_str=strings[0];
    for (int i=1;i<strings.size();i++)
    {
        if (strings[i].length()>longest_str.length())
        longest_str=strings[i];
    }
    return longest_str;
}
// or using std::max_element
#include<algorithm>
string longest(vector<string> strings){
    if (strings.size()==0)
    return "";
    return *std::max_element(strings.begin(), strings.end(), [](const string& a, const string& b)
    { return a.length() < b.length(); });
}  // end of C++ code
// end of code


