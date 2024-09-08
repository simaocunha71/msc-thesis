    vector<string> res;
    map<int,int> mp;
    int count=0;
    for(int i=0;i<lst.size();i++){
        for(int j=0;j<lst[i].size();j++){
            if(lst[i][j]%2!=0){
                count++;
            }
        }
        mp[i]=count;
        res.push_back(string("the number of odd elements ") + to_string(mp[i]) + " in the string " + to_string(i) + " of the input.");
        count=0;
    }
    return res;
} 





C:
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>

using namespace std;

vector<string> odd_count(vector<string> lst) {
    vector<string> res;
    map<int, int> mp;

    for (int i = 0; i < lst.size(); i++) {
        int count = 0;
        for (char c : lst[i]) {
            if (c - '0' % 2 != 0) {
                count++;
            }
        }
        mp[i] = count;
        stringstream ss;
        ss << "the number of odd elements " << mp[i] << " in the string " << i << " of the input.";
        res.push_back(ss.str());
    }

    return res;
}

int main() {
    vector<string> lst = {"1234567"};
    vector<string> result = odd_count(lst);

    for (string s : result) {
        cout << s << endl;
    }

    return 0;
} 





C++:
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>

using namespace std;

vector<string> odd_count(vector<string> lst) {
    vector<string> res;
    map<int, int> mp;

    for (int i = 0; i < lst.size(); i++) {
        int count = 0;
        for (char c : lst[i]) {
            if (c - '0' % 2 != 0) {
                count++;
            }
        }
        mp[i] = count;
        stringstream ss;
        ss << "the number of odd elements " << mp[i] << " in the string " << i << " of the input.";
        res.push_back(ss.str());
    }

    return res;
}

int main() {
    vector<string> lst = {"1234567", "111111