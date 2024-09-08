#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> get_odd_collatz(int n) {
        vector<int> result;
        int current = n;
        while (current != 1) {
            if (current % 2 != 0) {
                result.push_back(current);
            }
            current = current % 2 ? current * 3 + 1 : current / 2;
        }
        result.push_back(1);
        sort(result.begin(), result.end());
        return result;
    }
};

int main() {
    Solution s;
    vector<int> result = s.get_odd_collatz(5);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
B:
class Solution {
public:
    vector<int> get_odd_collatz(int n) {
        vector<int> result;
        int current = n;
        while (current != 1) {
            if (current % 2 != 0) {
                result.push_back(current);
            }
            current = current % 2 ? current * 3 + 1 : current / 2;
        }
        result.push_back(1);
        sort(result.begin(), result.end());
        return result;
    }
};
C:
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> get_odd_collatz(int n) {
    vector<int> result;
    int current = n;
    while (current != 1) {
        if (current % 2 != 0) {
            result.push_back(current);
        }
        current = current % 2 ? current * 3 + 1 : current / 2;
    }
    result.push_back(1);
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> result = get_odd_collatz(5);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
D:
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> get_odd_collatz(int n) {
    vector<int> result;
    int current = n;
    while (current != 1) {
        if (current % 2 != 0) {
