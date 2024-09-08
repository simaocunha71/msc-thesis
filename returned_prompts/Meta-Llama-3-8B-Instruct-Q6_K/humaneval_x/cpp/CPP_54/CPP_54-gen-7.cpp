    if(s0.length()!=s1.length())
        return false;
    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    for(int i=0;i<s0.length();i++)
        if(s0[i]!=s1[i])
            return false;
    return true;
} // same_chars

int main() {
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddeddabc"));  // true
    printf("%d\n",same_chars("abcd", "dddddddabc"));  // true
    printf("%d\n",same_chars("dddddddabc", "abcd"));  // true
    printf("%d\n",same_chars("eabcd", "dddddddabc"));  // false
    printf("%d\n",same_chars("abcd", "dddddddabce"));  // false
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddddabc"));  // false
    return 0;
} // main

B:
    string s0 = "eabcdzzzz";
    string s1 = "dddzzzzzzzddeddabc";

    if(s0.length()!=s1.length())
        cout << "false" << endl;
    else {
        sort(s0.begin(),s0.end());
        sort(s1.begin(),s1.end());
        for(int i=0;i<s0.length();i++)
            if(s0[i]!=s1[i])
                cout << "false" << endl;
        else
            cout << "true" << endl;
    }
    return 0; // B
} // main

C:
    bool same_chars(string s0, string s1) {
        if (s0.length() != s1.length()) {
            return false;
        }
        sort(s0.begin(), s0.end());
        sort(s1.begin(), s1.end());
        return s0 == s1;
    }

    int main() {
        cout << boolalpha;
        cout << same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") << endl;
        cout << same_chars("abcd", "dddddddabc") << endl;
        cout << same_chars("dddddddabc", "abcd") << endl;
        cout << same_chars("eabcd", "dddddddabc") << endl;
        cout << same_chars("abcd", "dddddddabce") << endl