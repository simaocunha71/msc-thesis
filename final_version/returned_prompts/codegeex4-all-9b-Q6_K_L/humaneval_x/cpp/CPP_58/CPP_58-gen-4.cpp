#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set<int> s3;

    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(s3, s3.begin()));
    return vector<int>(s3.begin(), s3.end());
}

int main(){
    vector<int> v1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> v2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> common_elements = common(v1, v2);
    copy(common_elements.begin(), common_elements.end(), ostream_iterator<int>(cout, " "));
    return 0;
}

B:
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

vector<int> common(vector<int> l1, vector<int> l2) {
    unordered_set<int> s1(l1.begin(), l1.end());
    unordered_set<int> s2(l2.begin(), l2.end());
    vector<int> common_elements;

    for (int i : s1) {
        if (s2.find(i) != s2.end()) {
            common_elements.push_back(i);
        }
    }

    sort(common_elements.begin(), common_elements.end());
    return common_elements;
}

int main() {
    vector<int> v1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> v2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> common_elements = common(v1, v2);
    for (int i : common_elements) {
        cout << i << " ";
    }
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

vector<int> common(vector<int> l1, vector<int> l2) {
    unordered_set<int> s1(l1.begin(), l1.end());
    unordered_set<int> s2(l2.begin(), l2