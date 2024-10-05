    vector<int> result;
    sort(arr.begin(), arr.end());
    int size = arr.size();
    for(int i = size - 1; i >= size - k; i--){
        result.push_back(arr[i]);
    }
    return result;
}

int main()
{
    vector<int> arr = {4, -4, 4};
    int k = 2;
    vector<int> res = maximum(arr,k);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

//This problem can be solved by using the sort function in C++ and then just selecting the last k elements from the sorted vector.
//The time complexity is O(n log n), where n is the length of the vector.
//The space complexity is O(k), where k is the number of elements to be returned.

//The given code is a simple implementation of the above approach. It sorts the array and then pushes the last k elements of the sorted array into the result vector. The result vector is then returned.
//The sort function is a built-in function in C++ that sorts the array in ascending order. The time complexity of the sort function is O(n log n), where n is the length of the array. The space complexity of the sort function is O(n), as it requires additional space to store the sorted array.

//The code is correct and will return the correct result for the given examples. However, it does not handle the case where k is 0. If k is 0, the function should return an empty vector, not the original vector.
//So, the function needs to be modified to handle this case.
//The function also needs to be modified to handle the case where k is greater than the size of the array. In this case, the function should return the original array.
//The function also needs to be modified to handle the case where the array contains negative numbers. The sort function sorts the array in ascending order, but the problem statement asks for the maximum k numbers, which can be negative.
//The function also needs to be modified to handle the case where the array contains duplicate numbers. The sort function sorts the array in asc