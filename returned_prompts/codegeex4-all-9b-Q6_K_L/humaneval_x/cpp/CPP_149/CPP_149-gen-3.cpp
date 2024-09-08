#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool compare(const string& a, const string& b) {
    if (a.size() == b.size()) {
        return a < b;
    }
    return a.size() < b.size();
}

vector<string> vector_sort(vector<string>& vec) {
    vector<string> result;
    for (const auto& str : vec) {
        if (str.size() % 2 == 0) {
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(), compare);
    return result;
}

int main() {
    vector<string> vec1 = {"aa", "a", "aaa"};
    vector<string> vec2 = {"ab", "a", "aaa", "cd"};

    vector<string> result1 = vector_sort(vec1);
    vector<string> result2 = vector_sort(vec2);

    // Print results
    for (const auto& str : result1) {
        cout << str << " ";
    }
    cout << endl;

    for (const auto& str : result2) {
        cout << str << " ";
    }
    cout << endl;

    return 0;
}

B:
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool compare(const string& a, const string& b) {
    if (a.size() == b.size()) {
        return a < b;
    }
    return a.size() < b.size();
}

vector<string> vector_sort(vector<string>& vec) {
    vector<string> result;
    for (const auto& str : vec) {
        if (str.size() % 2 == 0) {
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(), compare);
    return result;
}

int main() {
    vector<string> vec1 = {"aa", "a", "aaa"};
    vector<string> vec2 = {"ab", "a", "aaa", "cd"};

    vector<string> result1 = vector_sort(vec1);
    vector<string> result2 = vector_sort(vec2);

    // Print results
    for (const auto& str : result1) {
        cout << str << " ";
    }
    cout << endl;

    for (const auto& str : result2) {
        cout << str << " ";
    }
    cout << endl;

    return 0;
}

