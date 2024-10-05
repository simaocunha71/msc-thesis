    for(int i = 1; i < arr.size(); i++){
        if(arr[i] <= arr[i-1])
            return i-1;
    }
    return -1;
}  // return -1 if no such element exists
// 0-indexed array
// If no such element exists then return -1
// Input array will not contain duplicate values
// Time complexity O(n) where n is the size of the array
// Space complexity O(1) as we are not using any extra space.
