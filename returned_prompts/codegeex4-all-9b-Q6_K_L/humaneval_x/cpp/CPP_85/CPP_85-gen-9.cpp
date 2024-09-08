#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

int add(vector<int> lst) {
    vector<int> even = {};
    for (int i = 0; i < lst.size(); i += 2) {
        if (lst[i] % 2 == 0) {
            even.push_back(lst[i]);
        }
    }
    return accumulate(even.begin(), even.end(), 0);
}

