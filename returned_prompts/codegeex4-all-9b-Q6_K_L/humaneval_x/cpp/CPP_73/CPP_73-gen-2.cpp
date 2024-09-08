#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int smallest_change(vector<int> arr) {
    int n = arr.size();
    int i = 0, j = n - 1;
    int count = 0;
    while (i < j) {
        if (arr[i] != arr[j]) {
            count++;
        }
        i++;
        j--;
    }
    return count;
}
int main() {
    vector<int> arr1 = {1, 2, 3, 5, 4, 7, 9, 6};
    vector<int> arr2 = {1, 2, 3, 4, 3, 2, 2};
    vector<int> arr3 = {1, 2, 3, 2, 1};
    cout << "smallest_change({1,2,3,5,4,7,9,6}) == " << smallest_change(arr1) << endl;
    cout << "smallest_change({1, 2, 3, 4, 3, 2, 2}) == " << smallest_change(arr2) << endl;
    cout << "smallest_change({1, 2, 3, 2, 1}) == " << smallest_change(arr3) << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
using namespace std;

int smallest_change(vector<int> arr) {
    int n = arr.size();
    int count = 0;
    for (int i = 0; i < n / 2; i++) {
        if (arr[i] != arr[n - i - 1]) {
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> arr1 = {1, 2, 3, 5, 4, 7, 9, 6};
    vector<int> arr2 = {1, 2, 3, 4, 3, 2, 2};
    vector<int> arr3 = {1, 2, 3, 2, 1};

    cout << "smallest_change({1,2,3,5,4,7,9,6}) == " << smallest_change(arr1) << endl;
    cout << "smallest_change({1, 2, 3, 4, 