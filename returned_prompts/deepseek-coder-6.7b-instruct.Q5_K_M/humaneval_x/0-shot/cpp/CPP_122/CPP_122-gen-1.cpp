    int sum=0;
    for(int i=0;i<k;i++){
        if(arr[i]<=99 && arr[i]>=-99)
            sum+=arr[i];
    }
    return sum;
}

int main() {
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("%d", add_elements(arr,k));
    return 0;
}

*/

#include<iostream>
#include<vector>
using namespace std;

int add_elements(vector<int> arr,int k){
    int sum=0;
    for(int i=0;i<k;i++){
        if(abs(arr[i])<=99)
            sum+=arr[i];
    }
    return sum;
}

int main() {
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    cout<< add_elements(arr,k);
    return 0;
}
/*
Here, we are accepting an integer array and integer k as input. We then iterate over the first k elements of the array and add to sum if the absolute value of the current element is less than or equal to 99. We finally return the sum.
*/

//Time Complexity: O(n) where n is the value of k.
//Space Complexity: O(1) because we are not using any extra space that scales with the input size.

//This is a simple and efficient solution to the problem.

//Note: This solution assumes that the array elements are already within the valid range of -99 to 99. If this is not the case, you may need to add additional checks within the if statement to handle those elements.

//Note: The problem does not specify what to do with negative numbers, so this solution assumes that negative numbers with at most 2 digits are not valid. If you want to treat them as valid, you would need to remove the