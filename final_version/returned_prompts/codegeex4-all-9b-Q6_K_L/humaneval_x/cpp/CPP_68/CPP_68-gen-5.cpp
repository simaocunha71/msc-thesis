#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    vector<int> res;
    int min = arr[0];
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] <= min) {
            min = arr[i];
        }
    }
    if (min == arr[0]) {
        return res;
    } else {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == min) {
                res.push_back(min);
                res.push_back(i);
                return res;
            }
        }
    }
}

void print(vector<int> arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    print(pluck({4, 2, 3}));
    print(pluck({1, 2, 3}));
    print(pluck({}));
    print(pluck({5, 0, 3, 0, 4, 2}));
    return 0;
}

B:
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    vector<int> res;
    if (arr.empty()) {
        return res;
    }
    int min = arr[0];
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] <= min) {
            min = arr[i];
        }
    }
    if (min == arr[0]) {
        return res;
    } else {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == min) {
                res.push_back(min);
                res.push_back(i);
                return res;
            }
        }
    }
}

void print(vector<int> arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    print(pluck({4, 2, 3}));
    print(pluck({1, 2, 3}));
    print(pluck({}));
    print(pl