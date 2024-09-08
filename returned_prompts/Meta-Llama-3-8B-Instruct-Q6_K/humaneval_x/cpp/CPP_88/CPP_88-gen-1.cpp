    if(array.empty()) return array;
    int sum = array[0] + array.back();
    vector<int> new_array = array;
    if(sum % 2 == 0){
        sort(new_array.begin(), new_array.end(), greater<int>());
    }else{
        sort(new_array.begin(), new_array.end());
    }
    return new_array;
} // Return the sorted array. The sum of the first and last elements of the array is used to determine the sorting order.

