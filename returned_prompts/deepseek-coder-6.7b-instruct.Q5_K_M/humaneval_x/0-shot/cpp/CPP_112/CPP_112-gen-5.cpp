    string s1, s2;
    for (int i = 0; i < s.size(); i++){
        if (c.find(s[i]) == string::npos)
            s1 += s[i];
        else
            s2 += s[i];
    }
    reverse(s1.begin(), s1.end());
    string s3 = s1 + s2;
    string s4 = s3;
    reverse(s4.begin(), s4.end());
    vector<string> res;
    res.push_back(s3);
    if (s3 == s4)
        res.push_back("True");
    else
        res.push_back("False");
    return res;
}
int main(){
    vector<string> res = reverse_delete("abcde", "ae");
    printf("%s %s\n", res[0].c_str(), res[1].c_str());
    res = reverse_delete("abcdef", "b");
    printf("%s %s\n", res[0].c_str(), res[1].c_str());
    res = reverse_delete("abcdedcba", "ab");
    printf("%s %s\n", res[0].c_str(), res[1].c_str());
    return 0;
}

Output:
bcd False
acdef False
cdedc True
*/

The idea here is to first separate the characters in the string s that are in c and the ones that aren't. Then reverse the first string and append the second string to it, forming a new string. Check if this string is a palindrome by comparing it with its reverse.
*/
#include<bits/stdc++.h>
using namespace std;

vector<string> reverse_delete(string s, string c) {
    string first, second;
    for (char ch : s) {
        if (c.find(ch) == string::npos)
            first += ch;
        else
            second += ch;
    }
    reverse(first.begin(), first.end());
    string res = first + second;
    string rev = res;
   