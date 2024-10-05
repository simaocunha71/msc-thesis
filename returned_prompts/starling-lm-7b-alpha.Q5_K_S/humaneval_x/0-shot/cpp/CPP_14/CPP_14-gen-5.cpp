    vector<string> res;
    string temp;
    for(int i = 0; i < str.length(); i++){
        temp = "";
        for(int j = i; j < str.length(); j++){
            temp += str[j];
            res.push_back(temp);
        }
    }
    return res;
}



/*
Given a string, return a vector of all the substrings of the string, sorted from shortest to longest.
>>> all_substrings("abc")
["a", "ab", "abc", "b", "c"]
*/
vector<string> all_substrings(string str){
B:
    vector<string> res;
    for(int i = 0; i < str.length(); i++){
        for(int j = i; j <= str.length(); j++){
            res.push_back(str.substr(i, j - i));
        }
    }
    return res;
}






/*
Return the longest substring in the input string where all characters are unique
>>> longest_uniq_subs("aaabcb")
"bca"
>>> longest_uniq_subs("aaabbb")
""
*/
string longest_uniq_subs(string str){
C:
    string res = "";
    int j = 0;
    for(int i = 0; i < str.length(); i++){
        if(str.find(str[i], j) == str.find(str[i])){
            res += str[i];
            j++;
        }
    }
    return res;
}






/*
Given two strings, return a vector of all the unique substrings from string 1 that are also substrings of string 2.
>>> common_substrings("abcabc", "bc")
["bc", "c"]
>>> common_substrings("abcabc", "bca")
["a", "c"]
*/
vector<string> common_substrings(string str1, string str2){
D:
    vector<string> res;
    for(int i = 0; i < str1.length