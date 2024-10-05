    for(int i = 0; i < lst.size()-1; i++){
        if(lst[i] > lst[i+1]){
            return false;
        }
    }
    return true;
}
int main(){
    vector<int> lst = {1, 2, 3, 4, 5, 6, 7};
    if(is_sorted(lst)){
        printf("true");
    }
    else{
        printf("false");
    }
}





*/
#include <bits/stdc++.h>
using namespace std;

// Function to check if the array is sorted or not
bool isSorted(vector<int> arr) {
    int n = arr.size();

    // If the array contains duplicate elements, return false
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] == arr[i + 1]) {
            return false;
        }
    }

    // If the array is sorted in ascending order, return true
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }

    return true;
}

// Driver Code
int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7};

    if (isSorted(arr)) {
        cout << "true";
    } else {
        cout << "false";
    }
    return 0;
}

















































































































