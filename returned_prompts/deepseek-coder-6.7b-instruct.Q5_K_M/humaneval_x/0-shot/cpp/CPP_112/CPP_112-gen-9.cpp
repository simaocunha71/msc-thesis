    for (char ch: c) {
        s.erase(remove(s.begin(), s.end(), ch), s.end());
    }

    string s_rev = s;
    reverse(s_rev.begin(), s_rev.end());

    bool is_palindrome = s == s_rev;

    return {s, is_palindrome ? "True" : "False"};
}
int main()
{
    string s = "abcde", c = "ae";
    vector<string> result = reverse_delete(s,c);
    printf("%s,%s\n",result[0].c_str(),result[1].c_str());
    s = "abcdef"; c = "b";
    result = reverse_delete(s,c);
    printf("%s,%s\n",result[0].c_str(),result[1].c_str());
    s = "abcdedcba"; c = "ab";
    result = reverse_delete(s,c);
    printf("%s,%s\n",result[0].c_str(),result[1].c_str());
    return 0;
}

This is the C++ program to solve the problem. It uses the STL function `remove()` to remove the characters from the string s that are present in the string c. Then it reverses the string s and checks whether the string is a palindrome or not.
*/
