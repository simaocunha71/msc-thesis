#include <iostream>
#include <vector>
#include <string>
using namespace std;

string exchange(vector<int> lst1, vector<int> lst2) {
    int count1 = 0;
    int count2 = 0;
    for (int i = 0; i < lst1.size(); i++) {
        if (lst1[i] % 2 != 0) {
            count1++;
        }
    }
    for (int i = 0; i < lst2.size(); i++) {
        if (lst2[i] % 2 == 0) {
            count2++;
        }
    }
    if (count1 <= count2) {
        return "YES";
    } else {
        return "NO";
    }
}

int main() {
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2 = {1, 2, 3, 4};
    cout << exchange(lst1, lst2) << endl; // Output: YES

    lst1 = {1, 2, 3, 4};
    lst2 = {1, 5, 3, 4};
    cout << exchange(lst1, lst2) << endl; // Output: NO

    return 0;
} 
C:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string exchange(vector<int> lst1, vector<int> lst2) {
    int count1 = 0;
    int count2 = 0;
    for (int i = 0; i < lst1.size(); i++) {
        if (lst1[i] % 2 != 0) {
            count1++;
        }
    }
    for (int i = 0; i < lst2.size(); i++) {
        if (lst2[i] % 2 == 0) {
            count2++;
        }
    }
    if (count1 <= count2) {
        return "YES";
    } else {
        return "NO";
    }
}

int main() {
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2 = {1, 2, 3, 4};
    cout << exchange(lst1, lst2) << endl; // Output: YES

    lst1 = {1, 2, 3, 4};
    lst2 = {