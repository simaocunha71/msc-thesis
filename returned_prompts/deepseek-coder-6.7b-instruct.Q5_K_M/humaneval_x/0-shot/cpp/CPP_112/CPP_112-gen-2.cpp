    for(char ch:c){
        s.erase(remove(s.begin(),s.end(),ch),s.end());
    }
    string s_reverse=s;
    reverse(s_reverse.begin(),s_reverse.end());
    vector<string> result;
    result.push_back(s);
    if(s==s_reverse)
        result.push_back("True");
    else
        result.push_back("False");
    return result;
}


int main(){
    string s="abcde";
    string c="ae";
    vector<string> result=reverse_delete(s,c);
    for(string str:result){
        printf("%s\n",str.c_str());
    }
    return 0;
}

Output:
bcd
False
*/

// C++ program to delete characters from string s that are equal to any character in string c and then check if the string is palindrome.
// If the string is a palindrome, it returns the string and "True" else it returns the string and "False".

#include <bits/stdc++.h>
using namespace std;

vector<string> palindromeCheck(string s, string c) {
    for (char ch : c) {
        s.erase(remove(s.begin(), s.end(), ch), s.end());
    }
    string rev = s;
    reverse(rev.begin(), rev.end());
    vector<string> result;
    result.push_back(s);
    if (s == rev) {
        result.push_back("True");
    } else {
        result.push_back("False");
    }
    return result;
}

int main() {
    string s = "abcde";
    string c = "ae";
    vector<string> result = palindromeCheck(s, c);
    for (string str : result) {
        cout << str << endl;
    }
    return 0;
}

// C++ program to delete characters from string s that are equal to any character in string c and then