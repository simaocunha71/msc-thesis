#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){

    int a = 0, b = 0;
    for (int i : lst) {
        if (i < 0 && i > a) {
            a = i;
        }
        if (i > 0 && i < b) {
            b = i;
        }
    }
    vector<int> ans = {a, b};
    return ans;
}

int main() {
    vector<int> lst = {2, 4, 1, 3, 5, 7};
    for (int i : largest_smallest_integers(lst)) {
        printf("%d ", i);
    }
}






















































































































































