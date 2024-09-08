    vector<int> result;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i]%2 == 0 && (result.empty() || arr[i] < result[0])){
            result = {arr[i], i};
        }
    }
    return result;
}

int main() {
    // Test cases
    vector<int> test1 = {4,2,3};
    vector<int> test2 = {1,2,3};
    vector<int> test3 = {};
    vector<int> test4 = {5, 0, 3, 0, 4, 2};
    
    cout << "Test 1: ";
    for(auto x : pluck(test1)) cout << x << " ";
    cout << endl;
    cout << "Test 2: ";
    for(auto x : pluck(test2)) cout << x << " ";
    cout << endl;
    cout << "Test 3: ";
    for(auto x : pluck(test3)) cout << x << " ";
    cout << endl;
    cout << "Test 4: ";
    for(auto x : pluck(test4)) cout << x << " ";
    cout << endl;

    return 0;
}
//Output:
//Test 1: 2 1 
//Test 2: 2 1 
//Test 3: 
//Test 4: 0 1 
//Time Complexity: O(n)
//Space Complexity: O(1) because we are using a constant amount of space to store the result.  //


This program reads the input vector and checks each element to see if it is even. If it is, it checks if the result is empty or if the current element is smaller than the smallest even value found so far. If it is, it updates the result with the current element and its index. If the result is still empty at the end, it means there were no even values, so it returns an empty result. Otherwise, it returns the result. The time complexity is O(n) because it checks each element in the input vector once, and the space complexity is O(1) because it uses a constant amount of space to store the result.