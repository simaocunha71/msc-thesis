    int min_even_index = -1;
    int min_even_value = INT_MAX;
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] % 2 == 0 && arr[i] < min_even_value) {
            min_even_value = arr[i];
            min_even_index = i;
        }
    }
    if(min_even_index != -1) {
        return {min_even_value, min_even_index};
    } else {
        return {};
    }
}
// Test the function
int main() {
    vector<int> arr1 = {4,2,3};
    vector<int> arr2 = {1,2,3};
    vector<int> arr3 = {};
    vector<int> arr4 = {5, 0, 3, 0, 4, 2};
    cout << "Example 1: " << pluck(arr1)[0] << ", " << pluck(arr1)[1] << endl;
    cout << "Example 2: " << pluck(arr2)[0] << ", " << pluck(arr2)[1] << endl;
    cout << "Example 3: " << pluck(arr3)[0] << ", " << pluck(arr3)[1] << endl;
    cout << "Example 4: " << pluck(arr4)[0] << ", " << pluck(arr4)[1] << endl;
    return 0;
}  // END OF MAIN
// END OF CODE

