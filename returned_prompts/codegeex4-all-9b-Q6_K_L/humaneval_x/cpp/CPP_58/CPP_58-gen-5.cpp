#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
#include <unordered_set>
using namespace std;

vector<int> common(vector<int> l1, vector<int> l2) {
    unordered_set<int> s1(l1.begin(), l1.end());
    unordered_set<int> s2(l2.begin(), l2.end());
    vector<int> result;
    for (auto it = s1.begin(); it != s1.end(); ++it) {
        if (s2.count(*it)) {
            result.push_back(*it);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> result = common(l1, l2);
    for (int i = 0; i < result.size(); ++i) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

B:
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
#include <unordered_set>
using namespace std;

vector<int> common(vector<int> l1, vector<int> l2) {
    unordered_set<int> s1(l1.begin(), l1.end());
    unordered_set<int> s2(l2.begin(), l2.end());
    vector<int> result;
    for (auto it = s1.begin(); it != s1.end(); ++it) {
        if (s2.count(*it)) {
            result.push_back(*it);
        }
    }
    return result;
}

int main() {
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> result = common(l1, l2);
    for (int i = 0; i < result.size(); ++i) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

C:
#include <stdio.h>
#include <math.h>
#include <