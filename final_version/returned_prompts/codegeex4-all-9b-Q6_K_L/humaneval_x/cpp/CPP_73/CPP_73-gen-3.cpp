#include <vector>
#include <algorithm>
using namespace std;
int smallest_change(vector<int> arr) {
    int count = 0;
    int i = 0, j = arr.size() - 1;
    while (i < j) {
        if (arr[i] != arr[j]) {
            count++;
        }
        i++;
        j--;
    }
    return count;
}

B:
#include <vector>
#include <algorithm>
using namespace std;
int smallest_change(vector<int> arr) {
    int count = 0;
    for (int i = 0; i < arr.size() / 2; i++) {
        if (arr[i] != arr[arr.size() - i - 1]) {
            count++;
        }
    }
    return count;
}

C:
#include <vector>
#include <algorithm>
using namespace std;
int smallest_change(vector<int> arr) {
    int count = 0;
    vector<int> temp(arr);
    sort(temp.begin(), temp.end());
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] != temp[i]) {
            count++;
        }
    }
    return count;
}

D:
#include <vector>
#include <algorithm>
using namespace std;
int smallest_change(vector<int> arr) {
    int count = 0;
    vector<int> temp(arr);
    sort(temp.begin(), temp.end());
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] != temp[temp.size() - i - 1]) {
            count++;
        }
    }
    return count;
}

E:
#include <vector>
#include <algorithm>
using namespace std;
int smallest_change(vector<int> arr) {
    int count = 0;
    vector<int> temp(arr);
    sort(temp.begin(), temp.end());
    for (int i = 0; i < temp.size() / 2; i++) {
        if (temp[i] != temp[temp.size() - i - 1]) {
            count++;
        }
    }
    return count;
}

F:
#include <vector>
#include <algorithm>
using namespace std;
int smallest_change(vector<int> arr) {
    int count = 0;
    vector<int> temp(arr);
    sort(temp.begin(), temp.end());
    for (int i = 0; i < temp.size(); i++) {
        if (temp[i] != temp[temp.size() - i - 