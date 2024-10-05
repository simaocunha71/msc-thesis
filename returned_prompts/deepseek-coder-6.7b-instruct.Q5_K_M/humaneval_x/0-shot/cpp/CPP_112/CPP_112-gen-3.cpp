    for (char ch : c) {
        s.erase(std::remove(s.begin(), s.end(), ch), s.end());
    }
    string reversed_s = s;
    reverse(reversed_s.begin(), reversed_s.end());
    vector<string> result = {s, (s == reversed_s ? "True" : "False")};
    return result;
}

int main() {
    vector<string> res = reverse_delete("abcde","ae");
    printf("(%s,%s)\n", res[0].c_str(), res[1].c_str());
    res = reverse_delete("abcdef","b");
    printf("(%s,%s)\n", res[0].c_str(), res[1].c_str());
    res = reverse_delete("abcdedcba","ab");
    printf("(%s,%s)\n", res[0].c_str(), res[1].c_str());
    return 0;
}

*/

#include <bits/stdc++.h>
using namespace std;

pair<string, bool> reverse_delete(string s, string c) {
    for (char ch : c) {
        s.erase(remove(s.begin(), s.end(), ch), s.end());
    }
    string reversed_s = s;
    reverse(reversed_s.begin(), reversed_s.end());
    return make_pair(s, s == reversed_s);
}

int main() {
    auto res = reverse_delete("abcde", "ae");
    cout << "(" << res.first << "," << (res.second ? "True" : "False") << ")" << endl;
    res = reverse_delete("abcdef", "b");
    cout << "(" << res.first << "," << (res.second ? "True" : "False") << ")" << endl;
    res = reverse_delete("abcdedcba", "ab");
    cout << "(" << res.first << "," << (res.second ? "True" :