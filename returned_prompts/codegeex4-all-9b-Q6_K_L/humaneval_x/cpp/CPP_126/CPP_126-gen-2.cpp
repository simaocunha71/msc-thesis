#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool is_sorted(vector<int> lst){
    for (int i = 0; i < lst.size()-1; i++) {
        if (lst[i] > lst[i+1]) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<int> arr1 = {5};
    vector<int> arr2 = {1, 2, 3, 4, 5};
    vector<int> arr3 = {1, 3, 2, 4, 5};
    vector<int> arr4 = {1, 2, 3, 4, 5, 6};
    vector<int> arr5 = {1, 2, 3, 4, 5, 6, 7};
    vector<int> arr6 = {1, 3, 2, 4, 5, 6, 7};
    vector<int> arr7 = {1, 2, 2, 3, 3, 4};
    vector<int> arr8 = {1, 2, 2, 2, 3, 4};

    cout << is_sorted(arr1) << endl;
    cout << is_sorted(arr2) << endl;
    cout << is_sorted(arr3) << endl;
    cout << is_sorted(arr4) << endl;
    cout << is_sorted(arr5) << endl;
    cout << is_sorted(arr6) << endl;
    cout << is_sorted(arr7) << endl;
    cout << is_sorted(arr8) << endl;

    return 0;
}
B:
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool is_sorted(vector<int> lst){
    for (int i = 0; i < lst.size()-1; i++) {
        if (lst[i] > lst[i+1]) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<int> arr1 = {5};
    vector<int> arr2 = {1, 2, 3, 4, 5};
    vector<int> arr3 = {1, 3, 2, 4, 5};
    vector<int> arr4 = {1, 2, 3, 4, 5, 6};
    vector<int> arr5