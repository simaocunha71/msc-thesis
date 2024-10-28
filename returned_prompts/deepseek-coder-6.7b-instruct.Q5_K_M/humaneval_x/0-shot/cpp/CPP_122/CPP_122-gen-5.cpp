    int sum = 0;
    for(int i=0; i<k; i++){
        if(arr[i] < 10 || arr[i] > 99){
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    vector<int> arr{111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("%d", add_elements(arr, k));
    return 0;
}

*/

#include <iostream>
#include <vector>

using namespace std;

int add_elements(vector<int> arr, int k){
    int sum = 0;
    for(int i = 0; i < k; i++){
        if(arr[i] < 10 || arr[i] > 99){
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    vector<int> arr{111,21,3,4000,5,6,7,8,9};
    int k = 4;
    cout << add_elements(arr, k) << endl;
    return 0;
}

// CPP Program to solve the problem
// Output: 24
// Explanation: 21 + 3 = 24
// This is the sum of the elements with at most two digits from the first 4 elements of the array.

/*

Input: arr = {111,21,3,4000,5,6,7,8,9}, k = 4
Output: 24

Explanation: 
The first 4 elements in the array are 111, 21, 3, and 4000. 
The elements with at most two digits are 21 and 3, so their sum is 24.

*/

// CPP Program to solve the problem
// Output: 24
// Explanation: 21 + 3 = 24
// This is the sum of the elements with at most two dig