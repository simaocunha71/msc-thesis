    vector<string> prefixes;
    prefixes.push_back(str.substr(0,1));
    for(int i = 1; i < str.length(); i++) {
        prefixes.push_back(str.substr(0,i+1));
    }
    return prefixes;
}

/*
Return vector of all suffixes from shortest to longest of the input string
>>> all_suffixes("abc")
{"c", "bc", "abc"}
*/
vector<string> all_suffixes(string str){
B:
    vector<string> suffixes;
    suffixes.push_back(str.substr(str.length()-1));
    for(int i = str.length()-2; i >= 0; i--) {
        suffixes.push_back(str.substr(i,str.length()-i));
    }
    return suffixes;
}


/*
Return the longest common prefix of the two strings. If there is no common prefix, an empty string is returned.
>>> longest_common_prefix("abcde","axcy")
"a"
*/
string longest_common_prefix(string str1, string str2){
C:
    int n = min(str1.length(),str2.length());
    for(int i = 0; i < n; i++) {
        if(str1[i] != str2[i]) {
            return str1.substr(0,i);
        }
    }
    return str1.substr(0,n);
}


/*
Return the longest common suffix of the two strings. If there is no common suffix, an empty string is returned.
>>> longest_common_suffix("abcde","axcy")
"e"
*/
string longest_common_suffix(string str1, string str2){
D:
    int n = min(str1.length(),str2.length());
    for(int i = n-1; i >= 0; i--) {
        if(str1[str1.length()-i-1] != str2[str2.length()-i-1]) {
            return str1.substr(str1