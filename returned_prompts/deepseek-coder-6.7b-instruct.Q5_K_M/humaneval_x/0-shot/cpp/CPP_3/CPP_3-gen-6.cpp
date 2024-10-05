    int sum = 0;
    for (int i = 0; i < operations.size(); i++){
        sum += operations[i];
        if (sum < 0){
            return true;
        }
    }
    return false;
}

int main(){
    vector<int> operations1 = {1, 2, 3};
    vector<int> operations2 = {1, 2, -4, 5};
    printf(below_zero(operations1) ? "true\n" : "false\n");
    printf(below_zero(operations2) ? "true\n" : "false\n");
    return 0;
}




*/

// C++ Solution:
#include<iostream>
#include<vector>
using namespace std;

bool below_zero(vector<int> operations){
    int sum = 0;
    for (int i = 0; i < operations.size(); i++){
        sum += operations[i];
        if (sum < 0){
            return true;
        }
    }
    return false;
}

int main(){
    vector<int> operations1 = {1, 2, 3};
    vector<int> operations2 = {1, 2, -4, 5};
    cout << (below_zero(operations1) ? "true" : "false") << endl;
    cout << (below_zero(operations2) ? "true" : "false") << endl;
    return 0;
}






*/


// C Solution:
#include<stdio.h>
#include<stdbool.h>

bool below_zero(int operations[], int size){
    int sum = 0;
    for (int i = 0; i < size; i++){
        sum += operations[i];
        if (sum < 0){
            return true;
        }
    }
    return false;
}

int main(){
    int operations1[] = {1, 2, 3};
    int operations2[] = {1, 2, -4, 5};
   