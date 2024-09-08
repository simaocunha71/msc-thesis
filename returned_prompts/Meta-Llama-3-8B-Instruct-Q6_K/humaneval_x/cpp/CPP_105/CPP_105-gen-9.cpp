



C++ code to solve the problem:

```cpp
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

vector<string> by_length(vector<int> arr) {
    map<int, string> num_map = { {1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"} };
    vector<int> temp;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] >= 1 && arr[i] <= 9) {
            temp.push_back(arr[i]);
        }
    }
    sort(temp.begin(), temp.end());
    reverse(temp.begin(), temp.end());
    vector<string> result;
    for (int i = 0; i < temp.size(); i++) {
        result.push_back(num_map[temp[i]]);
    }
    return result;
}

int main() {
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string>