    int n = arr.size();
    if(n == 0) return true;
    int breakPoint = 0;
    for(int i = 0; i < n - 1; i++){
        if(arr[i] > arr[i+1]){
            breakPoint = i+1;
            break;
        }
    }
    int shiftPoint = breakPoint;
    while(shiftPoint < n && arr[shiftPoint] == arr[0]) shiftPoint++;
    if(shiftPoint == n) return true;
    return (arr[shiftPoint] >= arr[0]);
}

int main(){
    vector<int> arr = {3, 4, 5, 1, 2};
    if(move_one_ball(arr)){
        printf("true\n");
    } else {
        printf("false\n");
    }
    return 0;
}

*/

#include <iostream>
#include <vector>

using namespace std;

bool move_one_ball(vector<int> arr) {
    int n = arr.size();
    if (n == 0) return true;
    int breakPoint = 0;
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i+1]) {
            breakPoint = i+1;
            break;
        }
    }
    int shiftPoint = breakPoint;
    while (shiftPoint < n && arr[shiftPoint] == arr[0]) shiftPoint++;
    if (shiftPoint == n) return true;
    return (arr[shiftPoint] >= arr[0]);
}

int main() {
    vector<int> arr = {3, 4, 5, 1, 2};
    if (move_one_ball(arr)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
    return 0;
}

//test_move_one_ball.cpp
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.