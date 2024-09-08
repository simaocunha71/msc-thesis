#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string s = "o o| .| o| o| .| .| .| .| o o";
    vector<int> v;
    int i;
    for (i=0; i<s.length(); i++) {
        if (s[i] == '.') {
            v.push_back(1);
            i++;
        } else if (s[i] == 'o') {
            if (s[i+1] == '|') {
                v.push_back(2);
                i++;
            } else {
                v.push_back(4);
            }
        }
    }
    for (int j=0; j<v.size(); j++) {
        cout << v[j] << " ";
    }
    cout << endl;
    return 0;
}

