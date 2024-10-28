    vector<string> ans;
    int n = str.length();
    for(int i=0;i<=n;i++)
        ans.push_back(str.substr(0,i));
    return ans;
}


/*
Return vector of all suffixes from shortest to longest of the input string
>>> all_suffixes("abc")
{"c", "bc", "abc"}
*/
vector<string> all_suffixes(string str){

B:
    vector<string> ans;
    int n = str.length();
    for(int i=n;i>=0;i--)
        ans.push_back(str.substr(i-1,n-i+1));
    return ans;
}


/*
Return vector of all substrings from shortest to longest of the input string
>>> all_substrings("abc")
{"a", "b", "c", "ab", "ac", "bc", "abc"}
*/
vector<string> all_substrings(string str){

C:
    vector<string> ans;
    int n = str.length();
    for(int i=0;i<n;i++)
        for(int j=i;j<n;j++)
            ans.push_back(str.substr(i,j-i+1));
    return ans;
}


/*
Return vector of all permutations of the input string
>>> all_permutations("abc")
{"abc", "acb", "bac", "bca", "cab", "cba"}
*/
vector<string> all_permutations(string str){

D:
    vector<string> ans;
    if(str.length() == 0)
        return {""};
    sort(str.begin(),str.end());
    do{
        ans.push_back(str);
    }while(next_permutation(str.begin(),str.end()));
    return ans;
}


/*
Return vector of all palindromic substrings of the input string
>>> all_palindromes("abc")
{"a", "b", "c", "ab", "ba