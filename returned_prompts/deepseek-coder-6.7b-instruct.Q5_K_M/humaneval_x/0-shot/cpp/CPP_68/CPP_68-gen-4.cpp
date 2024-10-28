    vector<int> res;
    int smallest_even = INT_MAX, index = -1;
    for (int i = 0; i < arr.size(); i++){
        if (arr[i] < smallest_even && arr[i] % 2 == 0){
            smallest_even = arr[i];
            index = i;
        }
    }
    if (index != -1){
        res.push_back(smallest_even);
        res.push_back(index);
    }
    return res;
}
int main(){
    vector<int> arr{5, 0, 3, 0, 4, 2};
    vector<int> res = pluck(arr);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

// Time Complexity: O(n)
// Space Complexity: O(1)

// The above code is a C++ solution for the problem. The function pluck takes a vector of integers as an argument and returns a vector of two integers.
// The function iterates over the given vector, and for each element, it checks if the element is smaller than the current smallest even number and is even.
// If so, it updates the smallest even number and its index. Finally, if the smallest even number was found, it returns a vector containing the smallest even number and its index; otherwise, it returns an empty vector.
// The function works in O(n) time and O(1) space.

// The main function is used to test the function. It creates a vector of integers, calls the function with the vector as an argument, and prints the returned vector.
// The function should print the smallest even number and its index for the given vector. If there are no even numbers, it should print an empty vector.
// The function should pass all the test cases.
// The constraints of the problem are satisfied as the size of the vector is within the range of 1 to 10000.

// Note: This solution assumes that the index of the vector starts from 0. If the index should start from 1, the code should be modified accordingly.
// Also, the code