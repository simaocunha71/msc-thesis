    for(int i=arr.size()-1;i>0;i--){
        if(arr[i]<arr[i-1]){
            return i;
        }
    }
    return -1;
}

// Testing the function
int main() {
    vector<int> arr1 = {1,2,4,3,5};
    printf("%d\n", can_arrange(arr1));  // Expected output: 3

    vector<int> arr2 = {1,2,3};
    printf("%d\n", can_arrange(arr2));  // Expected output: -1

    return 0;
}

This solution will first go through the array in reverse order (from the end to the beginning), comparing each element to the element immediately before it. If it finds an element that is less than its predecessor, it will return the index of that element. If it does not find such an element, it will return -1.

Note: This solution assumes that the input vector will not contain duplicate values. If that is not the case, you would need to add a check to ensure that the vector does not contain duplicate values before running the function.
*/

// ---------------------

/*
