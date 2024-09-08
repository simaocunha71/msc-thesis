#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> by_length(vector<int> arr) {
  vector<string> result;
  map<int, string> m = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
  sort(arr.begin(), arr.end());
  for (int i = arr.size() - 1; i >= 0; i--) {
    if (arr[i] > 9 || arr[i] < 1) continue;
    result.push_back(m[arr[i]]);
  }
  return result;
}

int main() {
  vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
  vector<string> res = by_length(arr);
  for (const auto &s : res) {
    cout << s << " ";
  }
  cout << endl;
  return 0;
}
C:
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> by_length(vector<int> arr) {
  vector<string> result;
  map<int, string> m = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
  sort(arr.begin(), arr.end());
  for (int i = arr.size() - 1; i >= 0; i--) {
    if (arr[i] > 9 || arr[i] < 1) continue;
    result.push_back(m[arr[i]]);
  }
  return result;
}

int main() {
  vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
  vector<string> res = by_length(arr);
  for (const auto &s : res) {
    cout << s << " ";
  }
  cout << endl;
  return 0;
}
B:
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> by_length(vector<int> arr) {
  vector<string> result;
  map<int, string> m