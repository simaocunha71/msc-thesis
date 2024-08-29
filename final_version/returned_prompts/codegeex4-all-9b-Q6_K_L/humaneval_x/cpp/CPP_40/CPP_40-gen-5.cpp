#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

bool triples_sum_to_zero(vector<int> l) {
    sort(l.begin(), l.end());
    for (int i = 0; i < l.size() - 2; i++) {
        int left = i + 1;
        int right = l.size() - 1;
        while (left < right) {
            int sum = l[i] + l[left] + l[right];
            if (sum == 0) {
                return true;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    return false;
}

int main() {
    vector<int> l = {1, 3, 5, 0};
    bool result = triples_sum_to_zero(l);
    printf("%d\n", result);
    return 0;
}

B:
#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

bool triples_sum_to_zero(vector<int> l) {
    sort(l.begin(), l.end());
    for (int i = 0; i < l.size() - 2; i++) {
        int left = i + 1;
        int right = l.size() - 1;
        while (left < right) {
            int sum = l[i] + l[left] + l[right];
            if (sum == 0) {
                return true;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    return false;
}

int main() {
    vector<int> l = {1, 3, 5, 0};
    bool result = triples_sum_to_zero(l);
    cout << result;
    return 0;
}
C:
#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

bool triples_sum_to_zero(vector<int> l) {
    sort(l.begin(), l.end());
    for (int i = 0; i < l.size() - 2; i++) {
        int left = i + 1;
        int right = l.size() - 1;
        while (left < right) {
            int sum = l[i] + l[left] + l[right];
            if (sum == 0) {
                return true;
            } else if (sum < 0) {
                left++;
            }