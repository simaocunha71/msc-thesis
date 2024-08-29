#include <algorithm>
#include <vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst) {
    auto it = lst.begin();
    int a = 0, b = 0;
    bool has_negative = false;
    bool has_positive = false;
    while (it != lst.end()) {
        if (*it < 0 && *it < a) {
            a = *it;
            has_negative = true;
        }
        if (*it > 0 && *it > b) {
            b = *it;
            has_positive = true;
        }
        ++it;
    }
    if (!has_negative) a = 0;
    if (!has_positive) b = 0;
    return {a, b};
}

C:
#include <algorithm>
#include <vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst) {
    int a = 0, b = 0;
    if (lst.size() > 0) {
        a = *min_element(lst.begin(), lst.end());
        b = *max_element(lst.begin(), lst.end());
        if (a > 0) a = 0;
        if (b < 0) b = 0;
    }
    return {a, b};
}

D:
#include <algorithm>
#include <vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst) {
    int a = 0, b = 0;
    if (lst.size() > 0) {
        a = *min_element(lst.begin(), lst.end());
        b = *max_element(lst.begin(), lst.end());
        if (a > 0) a = 0;
        if (b < 0) b = 0;
    }
    return {a, b};
}

E:
#include <algorithm>
#include <vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst) {
    int a = 0, b = 0;
    if (lst.size() > 0) {
        a = *max_element(lst.begin(), lst.end());
        b = *min_element(lst.begin(), lst.end());
        if (a < 0) a = 0;
        if (b > 0) b = 0;
    }
    return {a, b};
}

F:
#include <algorithm>
#include <vector>
using namespace std;
vector<int> largest_sm