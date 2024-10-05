    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i] % 2 == 0 && i % 2 == 0) {
            sum += lst[i];
        }
    }
    return sum;
}
int main() {
    vector<int> lst = { 3, 3, 3, 3, 3 };
    int sum = solutions(lst);
    printf("%d", sum);
    return 0;
}


Ans:
#include<stdio.h>
#include<vector>
using namespace std;
int solutions(vector<int> lst) {
    int sum = 0;
    for (int i = 0; i < lst.size(); i += 2) {
        if (lst[i] % 2 == 1) {
            sum += lst[i];
        }
    }
    return sum;
}
int main() {
    vector<int> lst = { 3, 3, 3, 3, 3 };
    int sum = solutions(lst);
    printf("%d", sum);
    return 0;
}


