#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
map<int, string> num2str = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
vector<string> by_length(vector<int> arr) {
    vector<string> result;
    for (auto n : arr) {
        if (n >= 1 && n <= 9) {
            result.push_back(num2str[n]);
        }
    }
    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    return result;
}

C:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
map<int, string> num2str = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
vector<string> by_length(vector<int> arr) {
    vector<string> result;
    for (auto n : arr) {
        if (n >= 1 && n <= 9) {
            result.push_back(num2str[n]);
        }
    }
    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    return result;
}

D:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
map<int, string> num2str = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
vector<string> by_length(vector<int> arr) {
    vector<string> result;
    for (auto n : arr) {
        if (n >= 1 && n <= 9) {
            result.push_back(num2str[n]);
        }
    }
    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    return result;
}

E:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
