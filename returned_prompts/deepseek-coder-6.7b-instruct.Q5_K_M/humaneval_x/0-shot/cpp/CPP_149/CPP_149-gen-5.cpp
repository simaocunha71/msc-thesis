    vector<string> ans;
    vector<string>::iterator it;
    for(it = lst.begin(); it != lst.end(); ++it){
        if(it->length() % 2 == 0){
            ans.push_back(*it);
        }
    }
    sort(ans.begin(), ans.end());
    return ans;
}

*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> sorted_list_sum(vector<string> lst) {
    vector<string> ans;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            ans.push_back(s);
        }
    }
    sort(ans.begin(), ans.end());
    return ans;
}

int main() {
    vector<string> a1 = {"ab", "a", "aaa", "cd"};
    vector<string> a2 = sorted_list_sum(a1);
    for(string s : a2) {
        cout << s << " ";
    }
    cout << endl;
    return 0;
}
/*
Output:
ab cd
*/

*/

































































































































































































