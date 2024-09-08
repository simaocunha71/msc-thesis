    vector<int> res;
    res.push_back(3);
    if(n > 0){
        if(n % 2 == 0) res.push_back(1 + n / 2);
        else{
            res.push_back(tri(n - 1)[n - 1] + tri(n - 1)[n - 2] + tri(n - 1)[n]);
        }
        return tri(n - 1);
    }
    return res;
}
int main(){
    printf("%d\n", tri(3)[3]);
    return 0;
}
C:
// Tribonacci sequence
#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

vector<int> tri(int n) {
    vector<int> res;
    res.push_back(3);
    if(n > 0){
        if(n % 2 == 0) {
            res.push_back(1 + n / 2);
        } else {
            res.push_back(tri(n - 1)[n - 1] + tri(n - 1)[n - 2] + tri(n - 1)[n]);
        }
        return tri(n - 1);
    }
    return res;
}

int main() {
    printf("%d\n", tri(3)[3]);
    return 0;
}
C++:
// Tribonacci sequence
#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

vector<int> tri(int n) {
    vector<int> res;
    res.push_back(3);
    if(n > 0){
        if(n % 2 == 0) {
            res.push_back(1 + n / 2);
        } else {
            res.push_back(tri(n - 1)[n - 1] + tri(n - 1)[n - 2] + tri(n - 1)[n]);
        }
        return tri(n - 1);
    }
    return res;
}

int main() {
    printf("%d\n", tri(3)[3]);
    return 0;
}
C++:
// Tribonacci sequence
#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

vector<int> tri(int n) {
    vector<int> res;
    res.push_back(3);
    if(n > 0){
        if(n % 2 == 0) {
            res.push_back(1 + n / 2);
        } else {
            res