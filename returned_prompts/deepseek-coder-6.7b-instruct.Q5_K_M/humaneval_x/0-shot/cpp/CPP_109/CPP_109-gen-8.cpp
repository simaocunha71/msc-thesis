    int n = arr.size();
    if(n == 0)
        return true;
    int count = 0;
    for(int i = 0; i < n - 1; i++){
        if(arr[i] > arr[i + 1])
            count++;
    }
    if(arr[n - 1] > arr[0])
        count++;
    return count <= 1;
}

int main(){
    vector<int> arr{3, 4, 5, 1, 2};
    if(move_one_ball(arr))
        printf("true");
    else
        printf("false");
    return 0;
}
// The output of the program will be "true".
// This is because we can sort the vector {3, 4, 5, 1, 2} by performing one right shift operation.
// That is, shift the last element 2 to the start. The sorted vector will be {2, 3, 4, 5, 1}.
// So, the output will be "true".

// The time complexity of this solution is O(n), where n is the size of the input vector.
// The space complexity of this solution is O(1), as no extra space is used.
// The function move_one_ball checks if it is possible to sort the given vector by performing at most one right shift operation.
// It counts the number of pairs of elements that are not in non-decreasing order and if the count is more than 1 it returns false, else it returns true.
// For the case of the last element being greater than the first element, it increases the count by 1.
// The function returns true if the count is 0 or 1, else it returns false.
// The function also handles the case of an empty vector by returning true.
// The function is tested in the main function by passing a vector and printing the result.
// The output of the main function is "true".

// The code is written in C++ and it uses the STL vector for handling the array of integers.
// The function move_one_ball returns a boolean value indicating whether it is possible to sort the given vector by performing at most one right shift operation.
//