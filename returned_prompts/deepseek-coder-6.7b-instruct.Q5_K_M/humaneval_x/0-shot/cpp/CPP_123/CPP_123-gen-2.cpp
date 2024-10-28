    vector<int> collatz;
    while(n != 1){
        if(n % 2 != 0){
            collatz.push_back(n);
        }
        n = n % 2 ? n*3 + 1 : n / 2;
    }
    collatz.push_back(1);
    sort(collatz.begin(), collatz.end());
    return collatz;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<int> collatz = get_odd_collatz(n);
    for(int i = 0; i < collatz.size(); i++){
        printf("%d ", collatz[i]);
    }
    printf("\n");
    return 0;
}


*/

//code/c++/collatz.cpp
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> collatz;
    while(n != 1){
        if(n % 2 != 0){
            collatz.push_back(n);
        }
        n = n % 2 ? n*3 + 1 : n / 2;
    }
    collatz.push_back(1);
    sort(collatz.begin(), collatz.end());
    return collatz;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<int> collatz = get_odd_collatz(n);
    for(int i = 0; i < collatz.size(); i++){
        printf("%d ", collatz[i]);
    }
    printf("\n");
    return 0;
}

//code/c++/collatz_test.cpp
#include<iostream>
#include<vector>
#include "collatz.cpp"
using namespace std;

int main() {
    int n = 5;
    vector<int> collatz = get_odd_collatz(n);
   