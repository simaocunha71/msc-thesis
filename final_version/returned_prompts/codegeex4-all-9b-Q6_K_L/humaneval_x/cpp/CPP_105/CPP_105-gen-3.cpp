#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

map<int, string> num2str = {
    {1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"},
    {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}
};

vector<string> by_length(vector<int> arr) {
    vector<int> filtered = arr;
    filtered.erase(remove_if(filtered.begin(), filtered.end(), [](int a) { return a < 1 || a > 9; }), filtered.end());
    sort(filtered.begin(), filtered.end());
    reverse(filtered.begin(), filtered.end());
    vector<string> result;
    for (auto num : filtered) {
        result.push_back(num2str[num]);
    }
    return result;
}

int main() {
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> result = by_length(arr);
    for (const auto &str : result) {
        cout << str << " ";
    }
    cout << endl;
    return 0;
}
B:
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

map<int, string> num2str = {
    {1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"},
    {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}
};

vector<string> by_length(vector<int> arr) {
    vector<int> filtered = arr;
    filtered.erase(remove_if(filtered.begin(), filtered.end(), [](int a) { return a < 1 || a > 9; }), filtered.end());
    sort(filtered.begin(), filtered.end());
    reverse(filtered.begin(), filtered.end());
    vector<string> result;
    for (auto num : filtered) {
        result.push_back(num2str[num]);
    }
    return result;
}

int main() {
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> result = by_length(arr);
    for (const auto &str : result) {
        cout << str << " ";
    }
    cout <<