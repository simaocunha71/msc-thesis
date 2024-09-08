    if(s0.length()!=s1.length()){
        return false;
    }
    int i=0;
    while(i<s0.length()){
        if(s0[i]!=s1[i]){
            return false;
        }
        i++;
    }
    return true;
}

int main(){
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddeddabc"));
    printf("%d\n",same_chars("abcd", "dddddddabc"));
    printf("%d\n",same_chars("dddddddabc", "abcd"));
    printf("%d\n",same_chars("eabcd", "dddddddabc"));
    printf("%d\n",same_chars("abcd", "dddddddabce"));
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddddabc"));
    return 0;
}
B:
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
bool same_chars(string s0, string s1) {
    if (s0.size() != s1.size()) {
        return false;
    }
    sort(s0.begin(), s0.end());
    sort(s1.begin(), s1.end());
    return s0 == s1;
}

int main() {
    cout << (same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") ? "true" : "false") << endl;
    cout << (same_chars("abcd", "dddddddabc") ? "true" : "false") << endl;
    cout << (same_chars("dddddddabc", "abcd") ? "true" : "false") << endl;
    cout << (same_chars("eabcd", "dddddddabc") ? "true" : "false") << endl;
    cout << (same_chars("abcd", "dddddddabce") ? "true" : "false") << endl;
    cout << (same_chars("eabcdzzzz", "dddzzzzzzzddddabc") ? "true" : "false") << endl;
    return 0;
}
C:
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
bool same_chars(string s0, string s1) {
    if (s0.size() != s1.size()) {
        return false;
    }
    sort(s0.begin(), s0.end());
    sort(s1.begin(), s1.end());
    return s0 == s1;
}

int main